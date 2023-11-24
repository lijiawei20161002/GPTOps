import openai
import pandas as pd
import time
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

openai.api_key = "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"

file_path = "philly_output_summary.txt"
with open(file_path, 'r') as f:
    data = f.read().split("==================================================")

# Group data into sets of 2 records (1 for prediction and 1 for ground truth)
grouped_data = [data[i:i + 2] for i in range(0, len(data), 2)]

y_true = []
y_pred = []
y_pred_feedback = []

with open('group.txt', 'w') as f:
    for i, group in enumerate(grouped_data):
        if len(group[0].split('\n')) < 3:
            continue
        prediction_text = group[0].split('\n')[2]
        # Prediction template
        template = "Based on the prediction that {predicted_trend} for the upcoming {prediction_period}, provide the reasoning or logic behind this forecast and sequentially update or adjust the rules based on this prediction. Consider the entire dataset from the start until now, especially focusing on the distinctions between <current> and <history> data segments."
        prompt = template.format(predicted_trend=prediction_text, prediction_period="the next 60 min")  # you can adjust the prediction_period as needed
        prompt = [
            {"role": "user",
             "content": prompt}]
        true_text = group[1].split('\n')[2] if len(group) > 1 else ""

        # Prediction without feedback
        print(prompt)
        response = openai.ChatCompletion.create(
            model="gpt-4",
            temperature=0.5,
            messages=prompt
        )
        prediction = response['choices'][0]['message']['content']
        y_pred.append(prediction)

        # Prediction with feedback
        if i > 0 and len(y_true)>0:
            feedback_text = [
                {"role": "user",
                 "content": f"{prediction_text}\nTrue: {y_true[-1]}"}]
            print(feedback_text)
            response_feedback = openai.ChatCompletion.create(
                model="gpt-4",
                temperature=0.5,
                messages=feedback_text
            )
            prediction_feedback = response_feedback['choices'][0]['message']['content']
        else:
            prediction_feedback = prediction
        y_pred_feedback.append(prediction_feedback)

        y_true.append(true_text)

        # Write prediction and true value to file
        f.write(f"Group {i + 1}:\n")
        f.write(f"Prediction: {prediction}\n")
        f.write(f"Prediction with feedback: {prediction_feedback}\n")
        f.write(f"True: {true_text}\n")
        f.write("\n" + "=" * 50 + "\n")
        time.sleep(1)

# Calculate accuracy, precision, recall, and F1-score for prediction without feedback
accuracy = accuracy_score(y_true, y_pred)
precision = precision_score(y_true, y_pred, average='macro')
recall = recall_score(y_true, y_pred, average='macro')
f1 = f1_score(y_true, y_pred, average='macro')

# Calculate accuracy, precision, recall, and F1-score for prediction with feedback
accuracy_feedback = accuracy_score(y_true, y_pred_feedback)
precision_feedback = precision_score(y_true, y_pred_feedback, average='macro')
recall_feedback = recall_score(y_true, y_pred_feedback, average='macro')
f1_feedback = f1_score(y_true, y_pred_feedback, average='macro')

# Write the evaluation metrics to file
with open('evaluation_metrics.txt', 'w') as f:
    f.write("Without Feedback:\n")
    f.write(f"Accuracy: {accuracy}\n")
    f.write(f"Precision: {precision}\n")
    f.write(f"Recall: {recall}\n")
    f.write(f"F1-score: {f1}\n")
    f.write("\nWith Feedback:\n")
    f.write(f"Accuracy: {accuracy_feedback}\n")
    f.write(f"Precision: {precision_feedback}\n")
    f.write(f"Recall: {recall_feedback}\n")
    f.write(f"F1-score: {f1_feedback}\n")

print("Summaries and evaluation metrics written to files.")
