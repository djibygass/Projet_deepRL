class GridWorld:
    def __init__(self, size=5):
        self.size = size
        self.start_pos = (0, 0)  # Top-left corner
        self.win_pos = (self.size - 1, self.size - 1)  # Bottom-right corner
        self.lose_pos = (0, self.size - 1)  # Top-right corner
        self.reset()

    def reset(self):
        """Reset the environment to its starting state."""
        self.position = self.start_pos
        self.done = False
        return self.position

    def step(self, action):
        """Take an action in the environment."""
        if self.done:
            print("Game Over. Please reset the environment.")
            return

        x, y = self.position

        # Define the actions
        if action == 0 and x > 0:  # Move Up
            x -= 1
        elif action == 1 and x < self.size - 1:  # Move Down
            x += 1
        elif action == 2 and y > 0:  # Move Left
            y -= 1
        elif action == 3 and y < self.size - 1:  # Move Right
            y += 1

        self.position = (x, y)

        # Check for terminal states
        if self.position == self.lose_pos:
            reward = -1
            self.done = True
        elif self.position == self.win_pos:
            reward = 1
            self.done = True
        else:
            reward = 0

        return self.position, reward, self.done

    def render(self):
        """Visualize the environment."""
        board = [['_' for _ in range(self.size)] for _ in range(self.size)]
        x, y = self.position
        board[x][y] = 'P'
        return '\n'.join([''.join(row) for row in board])


# Test the environment
env_grid = GridWorld()
print(env_grid.render())
print(env_grid.step(3))  # Move Right
print(env_grid.render())
print(env_grid.step(3))  # Move Right
print(env_grid.render())
print(env_grid.step(3))  # Move Right
print(env_grid.render())
print(env_grid.step(3))  # Move Right
print(env_grid.render())
