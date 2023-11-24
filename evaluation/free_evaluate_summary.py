import os
import csv
import nltk
from rouge import Rouge
from nltk import word_tokenize
from sentence_transformers import SentenceTransformer, util
import numpy as np

class CoherenceModel:
    def __init__(self):
        self.model = SentenceTransformer('paraphrase-distilroberta-base-v2')

    def get_coherence(self, text):
        sentences = [s.strip() for s in text.split('.') if s]
        embeddings = self.model.encode(sentences, convert_to_tensor=True)
        avg_similarity = 0

        for i in range(len(sentences) - 1):
            cosine_scores = util.pytorch_cos_sim(embeddings[i], embeddings[i + 1])
            avg_similarity += cosine_scores.item()

        avg_similarity /= len(sentences) - 1
        return avg_similarity

def calculate_compression_ratio(original_text, summary):
    original_length = len(word_tokenize(original_text))
    summary_length = len(word_tokenize(summary))
    compression_ratio = summary_length / original_length
    return compression_ratio

def calculate_keyword_coverage(summary, keywords):
    summary_tokens = set(word_tokenize(summary))
    coverage = len(summary_tokens.intersection(keywords)) / len(keywords)
    return coverage

def calculate_coherence(summary, coherence_model):
    coherence_score = coherence_model.get_coherence(summary)
    return coherence_score

def calculate_consistency(summary):
    # Tokenize the summary into sentences
    sentences = word_tokenize(summary)

    # Initialize a counter for the number of consistent pairs of sentences
    consistent_pairs_count = 0

    # List of contradictory pairs of statements
    contradictory_pairs = [
    ("The CPU usage was low.", "The CPU usage was high."),
    ("Memory consumption was above average.", "Memory consumption was below average."),
    ("The CPU is not under heavy load.", "The CPU is under heavy load."),
    ("The system is not utilizing much memory.", "The system is utilizing a lot of memory."),
    ("CPU usage remained stable.", "CPU usage fluctuated significantly."),
    ("Memory usage was consistent.", "Memory usage was erratic."),
    ("The CPU is handling the processes efficiently.", "The CPU is struggling to handle the processes."),
    ("There is enough free memory available.", "There is not enough free memory available."),
    ("The CPU temperature is within normal range.", "The CPU temperature is above normal range."),
    ("Memory leaks are not present.", "Memory leaks are present."),
    ("The CPU is idle.", "The CPU is busy."),
    ("The memory is being used efficiently.", "The memory is not being used efficiently."),
    ("CPU usage is within the acceptable range.", "CPU usage is outside the acceptable range."),
    ("There are sufficient memory resources.", "There are insufficient memory resources.")
    ]

    # Loop through each pair of sentences
    for i in range(len(sentences)):
        for j in range(i + 1, len(sentences)):
            # Compare sentence i and sentence j
            if is_consistent(sentences[i], sentences[j], contradictory_pairs):
                consistent_pairs_count += 1

    # Calculate the consistency score as the ratio of consistent pairs to total pairs
    total_pairs = len(sentences) * (len(sentences) - 1) / 2
    consistency_score = consistent_pairs_count / total_pairs if total_pairs > 0 else 1.0

    return consistency_score

def is_consistent(sentence1, sentence2, contradictory_pairs):
    for pair in contradictory_pairs:
        if (sentence1 in pair and sentence2 in pair) or (sentence2 in pair and sentence1 in pair):
            return False
    return True

def main():
    summary_file_path = 'free_output_summary.txt'
    original_text_csv_file = 'free.csv'
    result_file_path = 'evaluation_results.txt'
    keywords = {'CPU', 'memory', 'usage', 'tier', 'hour'}
    records_per_group = 24

    coherence_model = CoherenceModel()

    with open(summary_file_path, 'r') as sf, open(original_text_csv_file, 'r', encoding='utf-8') as csvf, open(result_file_path, 'w') as rf:
        summaries = sf.read().split('=' * 50)
        reader = csv.DictReader(csvf)
        records = [row for row in reader]

        groups = [records[i:i + records_per_group] for i in range(0, len(records), records_per_group)]
        original_texts_per_group = [' '.join([' '.join(row.values()) for row in group]) for group in groups]

        for i, (summary, original_text) in enumerate(zip(summaries, original_texts_per_group)):
            summary = summary.strip()
            original_text = original_text.strip()

            rf.write(f'Group {i + 1}:\n')

            compression_ratio = calculate_compression_ratio(original_text, summary)
            keyword_coverage = calculate_keyword_coverage(summary, keywords)
            coherence = calculate_coherence(summary, coherence_model)
            consistency = calculate_consistency(summary)

            rf.write(f'Compression Ratio: {compression_ratio}\n')
            rf.write(f'Keyword Coverage: {keyword_coverage}\n')
            rf.write(f'Coherence: {coherence}\n')
            rf.write(f'Consistency: {consistency}\n')
            rf.write('-' * 50 + '\n')

if __name__ == '__main__':
    main()
