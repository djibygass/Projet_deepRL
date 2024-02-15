import random
import math
import numpy as np
import torch
import torch.nn as nn
import torch.optim as optim
from collections import deque
class RandomPlayer:
    def __init__(self):
        pass

    def choose_columns(self, possible_choices):
        # Randomly select an index from the possible choices based on dice roll
        return random.randint(0, len(possible_choices) - 1)
    
    def decide_continue(self):
        # Randomly decide whether to continue or stop
        return random.choice([True, False])
class MCTSNode:
    def __init__(self, game_state, parent=None, move=None):
        self.game_state = game_state
        self.parent = parent
        self.move = move
        self.children = []
        self.wins = 0
        self.visits = 1

    def is_fully_expanded(self):
        return len(self.children) == len(self.game_state.get_possible_choices())

    def best_child(self, c_param=1.4):
        choices_weights = [
            (child.wins / child.visits) + c_param * math.sqrt((2 * math.log(self.visits) / child.visits))
            for child in self.children
        ]
        return self.children[np.argmax(choices_weights)]

    def rollout(self):

        current_rollout_state = self.game_state.clone()
        for _ in range(50):  # Limiter à 50 tours pour éviter la boucle infinie
            if current_rollout_state.is_over():
                break
            possible_moves = current_rollout_state.get_possible_choices()
            action_idx = self.rollout_policy(possible_moves)
            current_rollout_state.select_choice(action_idx)

        return current_rollout_state.get_winner()

    def rollout_policy(self, possible_moves):
        # Retourne l'indice d'un mouvement choisi aléatoirement
        return random.randint(0, len(possible_moves) - 1)

    def backpropagate(self, result):
        self.visits += 1
        if self.parent:
            self.wins += 1 if self.parent.game_state.current_player == result else 0
            self.parent.backpropagate(result)

    def expand(self):

        for idx, choice in enumerate(self.game_state.get_possible_choices()):
            if idx not in [child.move for child in self.children]:
                new_game_state = self.game_state.clone()
                new_game_state.select_choice(idx)
                new_node = MCTSNode(new_game_state, parent=self, move=idx)
                self.children.append(new_node)


class MCTSPlayer:
    def __init__(self, iterations=100):
        self.iterations = iterations

    def choose_columns(self, game_state):

        root = MCTSNode(game_state)
        for _ in range(self.iterations):
            node = self._select_node(root)
            winner = node.rollout()
            node.backpropagate(winner)

        chosen_move = root.best_child(c_param=0).move

        return chosen_move
    def _select_node(self, node):

        while not node.game_state.is_over():
            if node.is_fully_expanded():

                node = node.best_child()
            else:

                node.expand()
                return node.children[-1]
        return node

    def decide_continue(self, game_state):
        # Continue tant que le jeu n'est pas terminé
        return not game_state.is_over()

class ReplayMemory:
    def __init__(self, capacity):
        self.memory = deque([], maxlen=capacity)

    def push(self, state, action, reward, next_state, done):
        self.memory.append((state, action, reward, next_state, done))

    def sample(self, batch_size):
        return random.sample(self.memory, batch_size)

    def __len__(self):
        return len(self.memory)
class DQNNetwork(nn.Module):
    def __init__(self, input_size, output_size):
        super(DQNNetwork, self).__init__()
        # Exemple de réseau simple
        self.layer1 = nn.Linear(input_size, 64)
        self.layer2 = nn.Linear(64, 64)
        self.output_layer = nn.Linear(64, output_size)

    def forward(self, x):
        x = torch.relu(self.layer1(x))
        x = torch.relu(self.layer2(x))
        return self.output_layer(x)
class DQNAgent:
    def __init__(self, state_size, action_size, memory_size=10000):
        self.state_size = state_size
        self.action_size = action_size
        self.memory = ReplayMemory(memory_size)
        self.model = DQNNetwork(state_size, action_size)
        self.optimizer = optim.Adam(self.model.parameters(), lr=0.001)

    def choose_columns(self, game_state):
        state = torch.from_numpy(np.array(game_state.encode_game_state())).float().unsqueeze(0)
        self.model.eval()
        with torch.no_grad():
            action_values = self.model(state)
        self.model.train()
        action_index = np.argmax(action_values.cpu().data.numpy())
        return min(action_index, len(game_state.get_possible_choices()) - 1)

    def learn(self, batch_size, gamma=0.99):
        if len(self.memory) < batch_size:
            return

        transitions = self.memory.sample(batch_size)
        batch_state, batch_action, batch_reward, batch_next_state, batch_done = zip(*transitions)

        # Convert to torch tensors
        batch_state = torch.tensor(batch_state, dtype=torch.float32)
        batch_action = torch.tensor(batch_action, dtype=torch.int64)
        batch_reward = torch.tensor(batch_reward, dtype=torch.float32)
        batch_next_state = torch.tensor(batch_next_state, dtype=torch.float32)
        batch_done = torch.tensor(batch_done, dtype=torch.float32)

        # Compute Q values
        current_q_values = self.model(batch_state).gather(1, batch_action.unsqueeze(1)).squeeze(1)
        next_q_values = self.model(batch_next_state).max(1)[0]
        expected_q_values = batch_reward + gamma * next_q_values * (1 - batch_done)

        # Compute loss
        loss = nn.functional.mse_loss(current_q_values, expected_q_values)

        # Optimize the model
        self.optimizer.zero_grad()
        loss.backward()
        self.optimizer.step()

    def decide_continue(self, game_state):
        return not game_state.is_over()


