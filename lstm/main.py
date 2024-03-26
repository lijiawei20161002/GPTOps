from numpy import array
import pandas as pd
from model import Benchmark_LSTM

def split_sequence(sequence, n_steps):
    X, y = list(), list()
    for i in range(len(sequence)):
        end_ix = i+n_steps
        if end_ix > len(sequence)-1:
            break
        seq_x, seq_y = sequence[i:end_ix], sequence[end_ix]
        X.append(seq_x)
        y.append(seq_y)
    return array(X), array(y)

data_path = '../tasks/dynamic vm pricing/data series/aws/p2.8xlarge_us-east-1a.txt'
raw_seq = pd.read_csv(data_path)['SpotPrice']
n_steps = 3
X, y = split_sequence(raw_seq, n_steps)
for i in range(len(X)):
    print(X[i], y[i])

n_features = 1
X = X.reshape((X.shape[0], X.shape[1], n_features))
model = Benchmark_LSTM(n_steps, n_features)
model.train(X, y, epochs=200)
yhat = model.predict(X[0:len(X)-n_steps])
print(yhat)