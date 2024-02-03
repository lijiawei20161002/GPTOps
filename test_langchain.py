from langchain.prompts.chat import (
    ChatPromptTemplate,
    HumanMessagePromptTemplate,
    SystemMessagePromptTemplate,
)
from langchain_community.chat_models import ChatOpenAI
from langchain.schema import HumanMessage, SystemMessage
import pandas as pd

chat = ChatOpenAI(temperature=0, openai_api_key="", openai_organization="")
template = "Given the recent data from our infrastructure logs: {log},\
              from {start_time} to {end_time},\
              provide a summary highlighting key\
              events and patterns in no more than {token_limit} tokens \
              The output summary should contain a \
                <current> part and a <history> part. The <current>\
                part represents the latest {latest_period}. The <history> part\
                represents history data begins from 0 seconds."
chat_prompt = ChatPromptTemplate.from_messages([
    SystemMessage(
        content="You are tasked with\
processing the numerical metrics provided by the Data\
Monitor. Convert these values into brief natural\
language text, providing a clear and accessible overview of\
the system’s current and historical state and performance."
    ),
    HumanMessagePromptTemplate.from_template(template),
])
filename = "free.csv"
df = pd.read_csv(filename)
n = len(df)
period=24
for i in range(0, n, period):
    log_data = df.iloc[i:min(i+period, n)].astype('str')
    summary = chat(chat_prompt.format_prompt(
            log=log_data, start_time=str(i), end_time=str(min(i+period, n)), token_limit="100", latest_period=str(period)+" hours"
        ).to_messages())
    print(summary.content)
    f = open(filename+".log", "a")
    f.write(summary.content)
    f.close()
