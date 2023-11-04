import random
class RandomPlayer:
    def __init__(self):
        pass

    def choose_columns(self, possible_choices):
        # Randomly select an index from the possible choices based on dice roll
        return random.randint(0, len(possible_choices) - 1)
    
    def decide_continue(self):
        # Randomly decide whether to continue or stop
        return random.choice([True, False])
