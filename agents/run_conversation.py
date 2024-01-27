from langchain.prompts.chat import (
    ChatPromptTemplate,
    HumanMessagePromptTemplate,
    SystemMessagePromptTemplate,
)
from langchain_community.chat_models import ChatOpenAI
from langchain.schema import HumanMessage, SystemMessage
from summary_agent import SummaryAgent

your_api_key = ''
your_org = ''
agent = SummaryAgent(openai_api_key=your_api_key, openai_organization=your_org)
agent.run()

