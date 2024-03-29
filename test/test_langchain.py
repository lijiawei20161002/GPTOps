from langchain.prompts.chat import (
    ChatPromptTemplate,
    HumanMessagePromptTemplate,
    SystemMessagePromptTemplate,
)
from langchain_community.chat_models import ChatOpenAI
from langchain.schema import HumanMessage, SystemMessage
import pandas as pd
import logging

# Setup Logging
logging.basicConfig(filename='test.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

chat = ChatOpenAI(temperature=0, openai_api_key="", openai_organization="")
template = "How are you?"
chat_prompt = ChatPromptTemplate.from_messages([
    SystemMessage(
        content=""
    ),
    HumanMessagePromptTemplate.from_template(template),
])
for i in range(20):
    output = chat(chat_prompt.format_prompt().to_messages())
    logging.info(output)
