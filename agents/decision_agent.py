from langchain.prompts.chat import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
)
from langchain_community.chat_models import ChatOpenAI
from langchain.schema import HumanMessage, SystemMessage

class DecisionAgent:
    def __init__(self, intention, openai_api_key, openai_organization):
        self.intention = intention
        self.openai_api_key = openai_api_key
        self.openai_organization = openai_organization
        self.chat = ChatOpenAI(temperature=0, openai_api_key=openai_api_key, openai_organization=openai_organization)
        self.template = self._create_template()

    def _create_template(self):
        return ChatPromptTemplate.from_messages([
            SystemMessage(
                content=f"Your task is to formulate actionable strategies. \
                        As a decision agent, your primary intention is to {self.intention}. \
                        Provide a clear <action> recommendation for the next action period. \
                        State your <confidence> in the recommendation, considering prediction inaccuracy and uncertainty. \
                        Explain the <reason> behind your decision into rules, detailing how various factors and data points influenced the recommendation."
            ),
            HumanMessagePromptTemplate.from_template("Based on the prediction {prediction_output} in next {prediction_period} days, \
                                                     provide your recommended <action>, <confidence>, <reason> for the next {action_period},\
                                                     in no more than {token_limit} tokens.\
                                                     Use blank space instead of comma after label <>.")
        ])
    
    def run(self, prediction_output, prediction_period, action_period, token_limit):
        decision = self.chat(self.template.format_prompt(
            prediction_output=prediction_output, prediction_period=str(prediction_period), action_period=str(action_period), token_limit=token_limit
        ).to_messages())
        return decision.content
