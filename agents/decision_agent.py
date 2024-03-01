from langchain.prompts.chat import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
)
from langchain_community.chat_models import ChatOpenAI
from langchain.schema import HumanMessage, SystemMessage

class DecisionAgent:
    def __init__(self, prediction_output, intention, action_period, openai_api_key, openai_organization):
        self.prediction_output = prediction_output
        self.intention = intention
        self.action_period = action_period
        self.openai_api_key = openai_api_key
        self.openai_organization = openai_organization
        self.chat = ChatOpenAI(temperature=0, openai_api_key=openai_api_key, openai_organization=openai_organization)
        self.template = self._create_template()

    def _create_template(self):
        return ChatPromptTemplate.from_messages([
            SystemMessage(
                content=f"Based on the prediction {self.prediction_output}, your task is to formulate actionable strategies. "
                        "As a decision agent, your primary intention is to {self.intention}. "
                        "Provide a clear <action> recommendation for the next {self.action_period}. "
                        "State your <confidence> in the recommendation, considering prediction inaccuracy and uncertainty. "
                        "Explain the <reason> behind your decision into rules, detailing how various factors and data points influenced the recommendation."
            ),
        ])
