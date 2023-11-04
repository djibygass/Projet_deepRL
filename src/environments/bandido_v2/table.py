from src.environments.bandido_v2.deck import Deck
from src.environments.bandido_v2.card import Card


class table:
    SIZE = Card.get_card_max_width() * Deck.get_deck_size()

    def __init__(self):
        self.table = [['' for _ in range(self.SIZE)] for _ in range(self.SIZE)]

    def is_placeable(self, card, x1, y1, x2, y2):
        # TODO: Implement the logic
        return False

    def drop_on_the_table(self, card, x1, y1, x2, y2):
        # TODO: Implement the logic
        return self
