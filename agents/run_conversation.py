from langchain.prompts.chat import (
    ChatPromptTemplate,
    HumanMessagePromptTemplate,
    SystemMessagePromptTemplate,
)
from langchain_community.chat_models import ChatOpenAI
from langchain.schema import HumanMessage, SystemMessage
from summary_agent import SummaryAgent

agent = SummaryAgent(openai_api_key="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", openai_organization="org-8yxc3dK5pYpaart4dR32FOda")
agent.run()

