import utils
import json
import pandas as pd

rawdata = utils.read_aws_prices("aws/cost/us-east-1", summary=False)
#rawdata = utils.read_azure_prices("azure/cost")
for key in rawdata.keys():
    df = pd.DataFrame(rawdata[key])
    #for zone in df[0].unique():
    #    price = df[df[0]==zone][[1, 2]]
    #    price = price.rename(columns={1: "Timestamp", 2: "SpotPrice"})
    for zone in df['AvailabilityZone'].unique():
        price = df[df['AvailabilityZone']==zone][['Timestamp', 'SpotPrice']]
        price = price.sort_values(by=['Timestamp'])
        price.to_csv(key+'_'+zone+'.txt', index=False)
