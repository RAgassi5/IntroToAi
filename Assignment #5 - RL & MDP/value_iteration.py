from typing import Tuple

import numpy as np
import math


class ValueIteration:

    def __init__(
        self,
        theta=0.0001,
        discount_factor=1.0,
    ):
        self.theta = theta
        self.discount_factor = discount_factor

    def calculate_q_values(
        self, current_capital: int, value_function: np.ndarray, rewards: np.ndarray
    ) -> np.ndarray:
        """
        Helper function to calculate the value for all action in a given state.

        Args:
            current_capital: The gambler’s capital. Integer. (state)
            value_function: The vector that contains values at each state. (the recursive value function)
            rewards: The reward vector. (the immediate reward according to the gambler's problem definition)

        Returns:
            A vector containing the expected value of each action in THIS state.
            Its length equals to the number of actions.
        """
        goal = 100

        # The gambler can bet up to their current capital, or up to the amount needed to reach 100.
        max_bet = min(current_capital, goal - current_capital)
        actions = np.arange(max_bet + 1)

        q_values = np.zeros(len(actions))

        # Probabilities based on the dice rolls:
        # 1. Sum < 7 (Probability 5/12): Lose the entire bet.
        prob_lose_all = 5 / 12
        # 2. Sum = 7 (Probability 2/12): Win the bet amount.
        prob_win = 2 / 12
        # 3. Sum > 7 (Probability 5/12): Lose half the bet (rounded up).
        prob_lose_half = 5 / 12

        for action in actions:
            if action == 0:
                # Action 0 means no change in state.
                state_val = rewards[current_capital] + self.discount_factor * value_function[current_capital]
                q_values[action] = state_val
                continue

            # Case 1: Lose entire bet (Sum < 7)
            s_lose_all = current_capital - action
            val_lose_all = rewards[s_lose_all] + self.discount_factor * value_function[s_lose_all]

            # Case 2: Win bet amount (Sum = 7)
            s_win = current_capital + action
            val_win = rewards[s_win] + self.discount_factor * value_function[s_win]

            # Case 3: Lose half bet, rounded up (Sum > 7)
            loss_amount = math.ceil(action / 2)
            s_lose_half = current_capital - loss_amount
            val_lose_half = rewards[s_lose_half] + self.discount_factor * value_function[s_lose_half]

            # Bellman Equation
            q_values[action] = (prob_lose_all * val_lose_all +
                                prob_win * val_win +
                                prob_lose_half * val_lose_half)

        return q_values

    def value_iteration_for_gamblers(self) -> Tuple[np.ndarray, np.ndarray]:
        """ """
        goal = 100
        # Initialize Value function with zeros
        V = np.zeros(goal + 1)

        # Initialize Rewards: 1 for the goal state (100), 0 for all others
        rewards = np.zeros(goal + 1)
        rewards[goal] = 1.0

        # Value Iteration Loop
        while True:
            delta = 0.0
            # Iterate over non-terminal states (1 to 99)
            for s in range(1, goal):
                old_v = V[s]

                # Calculate Q-values for all actions in state s
                q_values_s = self.calculate_q_values(s, V, rewards)

                # Greedy Update
                V[s] = np.max(q_values_s)

                # Update delta
                delta = max(delta, abs(old_v - V[s]))

            # Stop if converged
            if delta < self.theta:
                break

        # Policy Extraction
        policy = np.zeros(goal + 1)

        for s in range(1, goal):
            q_values_s = self.calculate_q_values(s, V, rewards)

            # Choose the action that maximizes the value.
            best_action = np.argmax(q_values_s)
            policy[s] = best_action

        # return policy, V
        return policy, V
