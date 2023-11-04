from src.environments.bandido_v2.exceptions import hand_full_exception


class Hand:
    HAND_SIZE = 3

    def __init__(self):
        self.cards = []

    @staticmethod
    def get_max_hand_size():
        return Hand.HAND_SIZE

    def get_cards(self):
        return self.cards

    def add_card(self, card):
        if len(self.cards) == Hand.HAND_SIZE:
            raise hand_full_exception()
        self.cards.append(card)

    def get_card(self, index):
        return self.cards[index]
