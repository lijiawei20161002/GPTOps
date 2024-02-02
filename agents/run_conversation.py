from langchain.prompts.chat import (
    ChatPromptTemplate,
    HumanMessagePromptTemplate,
    SystemMessagePromptTemplate,
)
from langchain_community.chat_models import ChatOpenAI
from langchain.schema import HumanMessage, SystemMessage
from summary_agent import SummaryAgent
from prediction_agent import PredictionAgent
import pandas as pd

your_api_key = ''
your_org = ''
token_limit = 100
latest_period = 10
fulldata = pd.read_csv('test_data.txt')
summary_agent = SummaryAgent(openai_api_key=your_api_key, openai_organization=your_org)
for i in range(0, len(fulldata), latest_period):
    start=i
    end=min(start+latest_period, len(fulldata))
    rawdata=fulldata[start:end]
    summary = summary_agent.run(rawdata=rawdata, start=start, end=end, token_limit=token_limit, latest_period=latest_period)
    print(summary)

#prediction_agent = PredictionAgent(openai_api_key=your_api_key, openai_organization=your_org)
#prediction_agent.run(summary=summary)

