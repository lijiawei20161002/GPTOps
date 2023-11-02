import openai
import pandas as pd

openai.api_key = "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"

# Load data from CSV file
file_path = "free.txt"  # Update this to the path of your CSV file
data = pd.read_csv(file_path)

# Ensure data is sorted and reset index
data = data.sort_values(by='hour_index').reset_index(drop=True)

# Group data into sets of 24 records
grouped_data = [data.iloc[i:i + 24] for i in range(0, len(data), 24)]

# Open file to output summaries
with open('output_summary.txt', 'w') as f:
    # Iterate through each group
    for i, group in enumerate(grouped_data):
        numerical_data = ""
        for index, row in group.iterrows():
            numerical_data += f"Hour: {row['hour_index']}, Tier: {row['tier']}, CPU Usage: {row['avg_cpu_usage']}, Memory Usage: {row['avg_memory_usage']}\n"

        start_time = group['hour_index'].iloc[0]
        end_time = group['hour_index'].iloc[-1]
        latest_period = end_time - start_time

        summary_prompt = [
            {"role": "user",
             "content": f'''Introduction: Given the recent data from our infrastructure logs: {numerical_data} \
Time Span: ...from {start_time} to {end_time} \
Task Description: ...provide a summary highlighting key events and patterns in no more than 50 tokens...\
Historical Data: ... The output summary should contain a <current> part and a <history> part. \
The <current> part represents the latest {latest_period}. \
The <history> part represents history data begins from 0 seconds.'''}
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

print("Summaries written to output_summary.txt")

