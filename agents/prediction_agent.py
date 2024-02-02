from langchain.prompts.chat import (
    ChatPromptTemplate,
    HumanMessagePromptTemplate,
    SystemMessagePromptTemplate,
)
from langchain_community.chat_models import ChatOpenAI
from langchain.schema import HumanMessage, SystemMessage
import pandas as pd

class PredictionAgent:
    def __init__(self, openai_api_key, openai_organization):
        self.chat = ChatOpenAI(temperature=0, openai_api_key=openai_api_key, openai_organization=openai_organization)
        self.template = "Given the current infrastructure status: {summarized_text}, from {start_time} to {end_time}, predict the trend of the infrastructure status in {prediction_period}. \
        considering the entire data from the start until now, where the latest {latest_period} data is labeled as <current> and the longer history is labeled as <history>.\
        Incorporate the following recent examples where predictions and their actual outcomes are given. Use these as a reference to enhance the accuracy of your current prediction:\
        {examples}\
        Output with label < prediction >. It should start with a brief overview stating the general trend expected in the next {prediction_period}, following by any relevant statistical \
        or probabilistic data that supports the prediction, and a conclusion summarizing the potential impact of these trends on the overall infrastructure status, in no more than {token_limit}.\
        Output the confidence of your prediction ranging from 0 to 1, with a label < confidence >."
        self.chat_prompt = ChatPromptTemplate.from_messages([
            SystemMessage(
                content="Your task is to analyze the summarized data received from the Summary Agent and forecast future trends and patterns of the various metrics. Leverage the predictive capabilities of GPT models to generate insights integral to informed decision-making."
            ),
            HumanMessagePromptTemplate.from_template(self.template),
        ])

    def run(self, summary, start, end, prediction_period, token_limit, latest_period, examples):
        prediction = self.chat(self.chat_prompt.format_prompt(
            summarized_text=summary, start_time=str(start), end_time=str(end), prediction_period=prediction_period, token_limit=token_limit, latest_period=str(latest_period), examples=examples
        ).to_messages())
        return prediction.context
