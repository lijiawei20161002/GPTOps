import openai
import pandas as pd
import time

openai.api_key = "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"

file_path = "philly.txt"
data = pd.read_csv(file_path, delimiter=',', header=0, skipinitialspace=True, on_bad_lines='skip')

# Ensure data is sorted by time and reset index
data = data.sort_values(by='time').reset_index(drop=True)

# Group data into sets of 60 records (or adjust as needed)
summary_period = 30
grouped_data = [data.iloc[i:i + summary_period] for i in range(0, len(data), summary_period)]

with open('philly_output_summary.txt', 'w') as f:
    for i, group in enumerate(grouped_data):
        numerical_data = ""
        
        for gpu_column in data.columns[2:]:
            for index, row in group.iterrows():
                numerical_data += f"Time: {row['time']}, Machine ID: {row['machineId']}, {gpu_column}: {row[gpu_column]}\n"
        
        start_time = group['time'].iloc[0]
        end_time = group['time'].iloc[-1]
        
        summary_prompt = [
            {"role": "user",
             "content": f'''Introduction: Given the recent data from our infrastructure logs: {numerical_data} \
Time Span: ...from {start_time} to {end_time} \
Task Description: ...provide a summary highlighting key events and patterns in no more than 50 tokens...\
Historical Data: ... The output summary should contain a <current> part and a <history> part. \
The <current> part represents the latest {summary_period} minutes. \
The <history> part represents history data begins from the start time of the file.'''}
        ]

        response = openai.ChatCompletion.create(
            model="gpt-4",
            temperature=0.5,
            messages=summary_prompt,
        )

        summary = response['choices'][0]['message']['content']

        # Write summary to file
        f.write(f"Group {i + 1}:\n")
        f.write(summary)
        f.write("\n" + "=" * 50 + "\n")
        time.sleep(1)

print("Summaries written to output_summary.txt")
