from keras.models import Sequential
from keras.layers import LSTM
from keras.layers import Dense

class Benchmark_LSTM:
    def __init__(self, n_steps, n_features):
        self.model = Sequential()
        self.model.add(LSTM(50, activation='relu', input_shape=(n_steps, n_features)))
        self.model.add(Dense(1))
        self.model.compile(optimizer='adam', loss='mse')

    def train(self, X, y, epochs=100, batch_size=32, verbose=1):
        self.model.fit(X, y, epochs=epochs, batch_size=batch_size, verbose=verbose)

    def predict(self, x_input):
        return self.model.predict(x_input)