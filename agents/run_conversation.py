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

your_api_key = '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'
your_org = 'org-8yxc3dK5pYpaart4dR32FOda'
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
    example='When input summary on from 0 to 10 days is: \
    <current> The latest data shows that the spot price for our infrastructure has been fluctuating between 0.3917 and 0.4019. There is a slight decrease in the spot price compared to the previous days. \
    <history> Looking at the historical data, we can see that the spot price has been relatively stable, with some minor fluctuations. On January 4th, there was a dip in the spot price to 0.3946, but it quickly recovered. \
    Overall, the spot price has remained within a narrow range over the past few days.\
     The output should be:\
     <prediction>: The most price will show a decreasing trend in the next 10 days, fluctuating between 0.3906 and 0.3683.  \
     This trend indicates potential cost savings for cloud infrastructure users in the market.\
     <confidence>: 0.95\
    '
    #prediction_agent = PredictionAgent(openai_api_key=your_api_key, openai_organization=your_org)
    #prediction_agent.run(summary=summary, start=start, end=end, prediction_period=latest_period, token_limit=token_limit, latest_period=latest_period, examples)

