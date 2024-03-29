from langchain.prompts.chat import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
)
from langchain_community.chat_models import ChatOpenAI
from langchain.schema import HumanMessage, SystemMessage

class ReflectionAgent:
    def __init__(self, openai_api_key, openai_organization):
        self.openai_api_key = openai_api_key
        self.openai_organization = openai_organization
        self.chat = ChatOpenAI(temperature=0, openai_api_key=openai_api_key, openai_organization=openai_organization)

    def interpret_prediction_algorithm(self, summary, prediction, token_limit):
        """
        Generates a Python function that encapsulates the logic from summary to prediction.
        """
        system_message = (
            "Given the following summary of the situation and the corresponding predictions, "
            "write a Python function that encapsulates the logic from summary to prediction. \n\n"
        )
        human_input = (
            f"Summary: {summary}\n"
            f"Prediction: {prediction}\n\n"
            "The Python function should take historical summary as input and return a prediction. "
            "Include comments in the code to explain how the function interprets the summary "
            "and how it arrives at the given prediction,"
            "in no more than {token_limit} tokens."
        )
        chat_prompt = ChatPromptTemplate.from_messages([
            SystemMessage(
                content=system_message
            ),
            HumanMessagePromptTemplate.from_template(human_input),
        ])
        response = self.chat(chat_prompt.format_prompt(summary=summary, prediction=prediction, token_limit=token_limit).to_messages())
        return response.content
    
    def adjust_prediction_algorithm(self, summary, prediction_algorithm, actual_outcomes, token_limit):
        """
        Adjusts the prediction algorithm based on the actual outcomes.
        """
        system_message = (
            "Given the Python function below that predicts future trends based on a summary, "
            "and the actual outcomes that differed from the prediction, adjust the Python function "
            "to improve its accuracy. Provide comments to explain the adjustments.\n\n"
        )
        human_input = (
            "Summary of the situation: {summary}\n"
            "Initial Python Prediction Algorithm: {prediction_algorithm}\n"
            "Actual Outcomes: {actual_outcomes}\n\n"
            "Adjusted Python Function:"
            "in no more than {token_limit}"
        )
        chat_prompt = ChatPromptTemplate.from_messages([
            SystemMessage(
                content=system_message
            ),
            HumanMessagePromptTemplate.from_template(human_input),
        ])
        response = self.chat(chat_prompt.format_prompt(summary=summary, prediction_algorithm=prediction_algorithm, actual_outcomes=actual_outcomes, token_limit=token_limit).to_messages())
        return response.content