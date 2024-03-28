import numpy as np

class DynamicVMProcurementQAgent:
    def __init__(self, n_states, n_actions, alpha=0.1, gamma=0.99, epsilon=0.1):
        """
        Initialize the Q-learning agent.
        
        :param n_states: Number of states (discretized if necessary)
        :param n_actions: Number of actions (2 in this case: 0 for not procuring, 1 for procuring)
        :param alpha: Learning rate
        :param gamma: Discount factor
        :param epsilon: Exploration rate
        """
        self.n_states = n_states
        self.n_actions = n_actions
        self.alpha = alpha
        self.gamma = gamma
        self.epsilon = epsilon
        self.q_table = np.zeros((n_states, n_actions))

    def choose_action(self, state):
        """
        Choose an action based on epsilon-greedy policy.
        
        :param state: The current state
        :return: Action (0 or 1)
        """
        if np.random.rand() < self.epsilon:
            return np.random.choice(self.n_actions)  # Explore
        else:
            return np.argmax(self.q_table[state])  # Exploit

    def update_q_table(self, state, action, reward, next_state):
        """
        Update the Q-value table using the Q-learning update rule.
        
        :param state: The current state
        :param action: The action taken
        :param reward: The reward received
        :param next_state: The next state
        """
        best_next_action = np.argmax(self.q_table[next_state])
        td_target = reward + self.gamma * self.q_table[next_state][best_next_action]
        td_error = td_target - self.q_table[state][action]
        self.q_table[state][action] += self.alpha * td_error

    def train(self, episodes, get_next_state_reward):
        """
        Train the Q-learning model.
        
        :param episodes: Number of episodes for training
        :param get_next_state_reward: Function to get the next state and reward given a state and action
        """
        for episode in range(episodes):
            state = np.random.randint(0, self.n_states)  # Random initial state
            done = False
            while not done:
                action = self.choose_action(state)
                next_state, reward, done = get_next_state_reward(state, action)
                self.update_q_table(state, action, reward, next_state)
                state = next_state
