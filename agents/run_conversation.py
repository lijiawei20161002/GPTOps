from langchain.prompts.chat import (
    ChatPromptTemplate,
    HumanMessagePromptTemplate,
    SystemMessagePromptTemplate,
)
from langchain_community.chat_models import ChatOpenAI
from langchain.schema import HumanMessage, SystemMessage
from summary_agent import SummaryAgent
from prediction_agent import PredictionAgent

your_api_key = ''
your_org = ''
summary_agent = SummaryAgent(openai_api_key=your_api_key, openai_organization=your_org)
summary = summary_agent.run()

prediction_agent = PredictionAgent(openai_api_key=your_api_key, openai_organization=your_org)
prediction_agent.run(summary=summary)

