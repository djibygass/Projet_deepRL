class LineWorld:
    def __init__(self, size=5):
        self.size = size
        self.start_pos = self.size // 2
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

        # Action 0: Move Left
        # Action 1: Move Right
        if action == 0 and self.position > 0:
            self.position -= 1
        elif action == 1 and self.position < self.size - 1:
            self.position += 1

        # Check for terminal states
        if self.position == 0:
            reward = -1
            self.done = True
        elif self.position == self.size - 1:
            reward = 1
            self.done = True
        else:
            reward = 0

        return self.position, reward, self.done

    def render(self):
        """Visualize the environment."""
        board = ['_'] * self.size
        board[self.position] = 'P'
        return ''.join(board)


# Test the environment
env = LineWorld()
print(env.render())
print(env.step(1))  # Move Right
print(env.render())
print(env.step(1))  # Move Right
print(env.render())
print(env.step(1))  # Move Right
print(env.render())
print(env.step(1))  # Move Right
print(env.render())

# show me step to put this projet on github
# git init
# git add .
# git commit -m "first commit"
# git branch -M main
# git remote add origin
# git@github...



