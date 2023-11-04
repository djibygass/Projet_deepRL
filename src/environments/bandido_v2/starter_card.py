from src.environments.bandido_v2.card import Card
from src.environments.bandido_v2.exceptions.invalid_card_exception import invalid_card_exception
from src.environments.bandido_v2.settings.difficulty_enum import Difficulty


class starter_card:

    @staticmethod
    def get_starter_card(difficulty):
        try:
            if difficulty == Difficulty.EASY:
                return Card("000111111000")  # it presents 4 exit paths
            return Card("010111111010")  # it presents 6 exit paths
        except invalid_card_exception as e:
            print(e)
            return None
