import pandas as pd
import logging
import os
import re

# Assuming these are your custom modules for demonstration
from summary_agent import SummaryAgent
from prediction_agent import PredictionAgent
from decision_agent import DecisionAgent

# Setup Logging
logging.basicConfig(filename='conversations.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

class VMPriceMonitoringSystem:
    def __init__(self, data_path):
        self.data_path = data_path
        self.token_limit = 100
        self.latest_period = 10
        self.history = ''
        self.intention = "Procure 1 VM, running 10 consecutive timesteps at the lowest spot prices."
        self.summary_agent = SummaryAgent(openai_api_key=os.getenv('OPENAI_API_KEY'), openai_organization=os.getenv('OPENAI_ORGANIZATION'))
        self.prediction_agent = PredictionAgent(openai_api_key=os.getenv('OPENAI_API_KEY'), openai_organization=os.getenv('OPENAI_ORGANIZATION'))
        self.decision_agent = DecisionAgent(intention=self.intention, openai_api_key=os.getenv('OPENAI_API_KEY'), openai_organization=os.getenv('OPENAI_ORGANIZATION'))
    
    def parse_agent_output(self, output):
        """Parses the formatted string output from an agent into a dictionary."""
        labels = ['current', 'history', 'prediction', 'confidence', 'reason', 'Action', 'Confidence', 'Reason']
        parsed_output = {}
        # Sort labels by length in descending order to avoid partial matches (longest match first)
        labels.sort(key=len, reverse=True)
        # Pattern to find the label and the text up until the next label or end of the string
        pattern = r"<(" + "|".join(labels) + ")>(.*?)\s*(?=<(" + "|".join(labels) + ")>|$)"
        matches = re.finditer(pattern, output, re.DOTALL)
        for match in matches:
            label = match.group(1)  
            content = match.group(2).strip()  
            parsed_output[label.lower()] = content

        return parsed_output
    
    def log_formatted_message(self, start, end, summary, prediction, decision):
        log_message = "\n\n"  # Start with new lines for separation
        if 'history' in summary:
            log_message += f"Summary for data from {start} to {end}:\n<current> {summary['current']}\n<history> {summary['history']}\n"
            log_message += "--------------------------------------------------\n"
        if 'prediction' in prediction and 'confidence' in prediction:
            log_message += f"Prediction for the next {str(self.latest_period)} days:\n<prediction>: {prediction['prediction']}\n<confidence>: {prediction['confidence']}\n"
            log_message += "--------------------------------------------------\n"
        if 'action' in decision and 'confidence' in decision and 'reason' in decision:
            log_message += f"Decision based on prediction:\n<Action>: {decision['action']}\n<Confidence>: {decision['confidence']}\n<Reason>: {decision['reason']}\n"
        logging.info(log_message)
    
    def run_cycle(self):
        try:
            fulldata = pd.read_csv(self.data_path)['SpotPrice']
        except Exception as e:
            logging.error(f"Failed to load data: {e}")
            return
        
        example="When input summary on from 0 to 10 days is: \
            <current> The latest data shows that the spot price for our infrastructure has been fluctuating between 0.3917 and 0.4019. \
            There is a slight decrease in the spot price compared to the previous days. \
            <history> Looking at the historical data, we can see that the spot price has been relatively stable, with some minor fluctuations. \
            On January 4th, there was a dip in the spot price to 0.3946, but it quickly recovered. \
            Overall, the spot price has remained within a narrow range over the past few days.\
            The output should be:\
            <prediction>: The most price will show a decreasing trend in the next 10 days, fluctuating between 0.3906 and 0.3683.  \
            This trend indicates potential cost savings for cloud infrastructure users in the market.\
            <confidence>: 0.95\
            "
        for i in range(0, len(fulldata), self.latest_period):
            start = i
            end = min(start + self.latest_period, len(fulldata))
            rawdata = fulldata[start:end]

            try:
                summary = self.summary_agent.run(rawdata=rawdata, start=start, end=end, history=self.history, token_limit=self.token_limit, latest_period=self.latest_period)
                prediction = self.prediction_agent.run(summary=summary, start=start, end=end, prediction_period=self.latest_period, token_limit=self.token_limit, latest_period=self.latest_period, examples=example)
                decision = self.decision_agent.run(prediction_output=prediction, prediction_period=self.latest_period, action_period=self.latest_period, token_limit=self.token_limit)
                self.log_formatted_message(str(start), str(end), self.parse_agent_output(summary), self.parse_agent_output(prediction), self.parse_agent_output(decision))

            except Exception as e:
                logging.error(f"Error during processing from {start} to {end}: {e}")