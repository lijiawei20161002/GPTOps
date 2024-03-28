from langchain.prompts.chat import (
    ChatPromptTemplate,
    HumanMessagePromptTemplate,
    SystemMessagePromptTemplate,
)
from langchain_community.chat_models import ChatOpenAI
from langchain.schema import HumanMessage, SystemMessage
import pandas as pd

class SummaryAgent:
    def __init__(self, openai_api_key, openai_organization):
        self.chat = ChatOpenAI(temperature=0, openai_api_key=openai_api_key, openai_organization=openai_organization)
        self.template = "Given the recent data from our infrastructure logs: {log}, from {start_time} to {end_time}, and {history}, \
            provide a summary highlighting key events and patterns in no more than {token_limit} tokens. \
            The output summary should contain a <current> part and a <history> part. \
            The <current> part represents the latest {latest_period}. \
            The <history> part represents history data begins from 0 seconds."
        self.chat_prompt = ChatPromptTemplate.from_messages([
            SystemMessage(
                content="You are tasked with processing the numerical metrics provided by the Data Monitor. \
                    Convert these values into brief natural language text, \
                    providing a clear and accessible overview of the system’s current and historical state and performance.\
                "
            ),
            HumanMessagePromptTemplate.from_template(self.template),
        ])

    def run(self, rawdata, start, end, history, token_limit, latest_period):
        summary = self.chat(self.chat_prompt.format_prompt(
            log=rawdata, start_time=str(start), end_time=str(end), history=history, token_limit=token_limit, latest_period=str(latest_period)
        ).to_messages())
        return summary.content
