from typing import List, Tuple

import gymnasium as gym
import numpy as np

SEED = 63

# Set the seed
rng = np.random.default_rng(SEED)


class Qlearning:
    def __init__(
        self,
        learning_rate: float,
        gamma: float,
        state_size: int,
        action_size: int,
        epsilon: float,
    ):
        self.state_size = state_size
        self.action_space_size = action_size
        self.learning_rate = learning_rate
        self.gamma = gamma
        self.epsilon = epsilon
        self.qtable = np.zeros((state_size, action_size))

    def update(self, state: int, action: int, reward: float, new_state: int):
        """In this function you need to implement the update of the Q-table.

        Args:
            state (int): Current state
            action (int): Action taken in the current state
            reward (float): Reward received after taking the action
            new_state (int): New state reached after taking the action.
        """
        # Q-Learning update formula learnt in class:
        # Q(s,a) = Q(s,a) + alpha * [reward + gamma * max(Q(s',a')) - Q(s,a)]

        # Calculate the maximum Q-value for the next state
        max_next_q = np.max(self.qtable[new_state, :])

        # Calculate the Target
        td_target = reward + self.gamma * max_next_q

        # Update the Q-value
        current_q = self.qtable[state, action]
        self.qtable[state, action] = current_q + self.learning_rate * (td_target - current_q)

    def reset_qtable(self):
        """Reset the Q-table."""
        self.qtable = np.zeros((self.state_size, self.action_space_size))

    def select_epsilon_greedy_action(self, state: int) -> int:
        """Select an action from the Q-table."""
        # Exploration
        if rng.random() < self.epsilon:
            return int(rng.integers(self.action_space_size))

        # Exploitation
        else:
            q_values = self.qtable[state, :]
            max_val = np.max(q_values)

            # Find all sections that have the maximum Q-value
            best_actions = np.where(q_values == max_val)[0]

            # Randomly choose one of the best actions
            return rng.choice(best_actions)

    def train_episode(self, env: gym.Env) -> Tuple[float, int]:
        """Train the agent for a single episode.

        Notice an episode is a single run of the environment until the agent reaches a terminal state
        (the return value of env.step() is True for the third and fourth elements)


        :param env: The environment to train the agent on.
        :return: the cumulative reward obtained during the episode and the number of steps executed in the episode.
        """
        state, _ = env.reset()
        total_reward = 0.0
        steps = 0
        terminated = False
        truncated = False

        # Loop until the episode is done (either terminated or truncated)
        while not (terminated or truncated):
            # Select action
            action = self.select_epsilon_greedy_action(state)

            # Do the action
            new_state, reward, terminated, truncated, _ = env.step(action)

            # Update Q-table
            self.update(state, action, reward, new_state)

            # Update state and reward
            state = new_state
            total_reward += reward
            steps += 1

        return total_reward, steps

    def run_environment(
        self, env: gym.Env, num_episodes: int
    ) -> Tuple[List[float], List[int]]:
        """
        Run the environment with the given policy.

        Args:
            env (gym.Env): The environment to train the agent on.
            num_episodes (int): The number of episodes to run the environment.

        Returns:
            A tuple (total_rewards, total_steps).
        """
        total_rewards = []
        total_steps = []

        for _ in range(num_episodes):
            episode_reward, episode_steps = self.train_episode(env)
            total_rewards.append(episode_reward)
            total_steps.append(episode_steps)

        return total_rewards, total_steps
