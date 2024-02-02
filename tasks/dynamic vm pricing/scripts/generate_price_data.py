import utils
import json
import pandas as pd

rawdata = utils.read_aws_prices("aws/cost/us-east-1", summary=False)
for key in rawdata.keys():
    df = pd.DataFrame(rawdata[key])
    for zone in df['AvailabilityZone'].unique():
        df[df['AvailabilityZone']==zone][['Timestamp', 'SpotPrice']].to_csv(key+'_'+zone+'.txt', index=False)
