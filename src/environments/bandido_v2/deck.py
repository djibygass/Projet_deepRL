from src.environments.bandido_v2.exceptions import empty_deck_exception, hand_full_exception
from src.environments.bandido_v2.hand import Hand


class Deck:
    DECK_SIZE = 69

    def __init__(self):
        self.deck = []

    @staticmethod
    def get_deck_size():
        return Deck.DECK_SIZE

    def get_cards(self):
        return self.deck

    def drop_hand(self):
        if not self.deck:
            raise empty_deck_exception()

        hand = Hand()
        for i in range(Hand.get_max_hand_size()):
            card = self.deck.pop()
            try:
                hand.add_card(card)
            except hand_full_exception:
                self.deck.append(card)
                break

        return hand

    def draw_card(self):
        if not self.deck:
            raise empty_deck_exception()

        return self.deck.pop()
