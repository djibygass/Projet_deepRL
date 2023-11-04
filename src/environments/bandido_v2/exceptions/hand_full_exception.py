from src.environments.bandido_v2.hand import Hand


class hand_full_exception(Exception):

    def __init__(self):
        # Assuming you've converted the Hand class to Python and imported it
        self.message = f"The hand is already full. It can be composed of max {Hand.get_max_hand_size()} cards."
        super().__init__(self.message)
