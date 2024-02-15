class Scoresheet:
    def __init__(self):
        self.scoresheet = {
            'Yellow': [0, 3, 7, 11, 15, 3],
            'Blue': [1, 3, 5, 7, 9, 12, 8],
            'Red': [0, 0, 0, 2, 4, 6, 8, 10, 14, 6],
            'Star': [1, 2, 3, 5, 7, 10, 13, 16, 4],
            'Moon': [2, 3, 4, 5, 7, 9, 12, 5],
            'Diamond': [1, 3, 6, 10, 13, 7]
        }
        self.current_positions = {key: -1 for key in self.scoresheet}
        self.breaks = [0, 0, 0]  # Scores for each of the three breaks
        self.total_score = 0
        self.num_breaks_triggered = 0

    def record_roll(self, results):
        # Update positions based on the dice rolled
        break_triggered = False
        for color, shape in results:
            for key in [color, shape]:
                if self.current_positions[key] < len(self.scoresheet[key]) - 1:
                    self.current_positions[key] += 1
                    # Check if the last number is reached (which means a break)
                    if self.current_positions[key] == len(self.scoresheet[key]) - 1:
                        break_triggered = True

        # Trigger a break if needed
        if break_triggered:
            self.trigger_break()

    def get_current_score(self):
        score = 0
        for key, position in self.current_positions.items():
            if position >= 0:  # Check if the column has been started
                score += self.scoresheet[key][position]
        return score

    def check_for_breaks(self):
        # Check if any 'Break' is triggered
        for key, pos in self.current_positions.items():
            if pos >= 0 and self.scoresheet[key][pos] == 'Break':
                return True
        return False

    def trigger_break(self):
        # Only trigger if less than 3 breaks have occurred
        if self.num_breaks_triggered < 3:
            # Calculate and record the score for this break
            self.breaks[self.num_breaks_triggered] = self.calculate_break_score()
            self.num_breaks_triggered += 1
            self.calculate_total_score()

    def calculate_break_score(self):
        # Calculate the score at the moment of the break
        score = 0
        for key, position in self.current_positions.items():
            if position >= 0:
                # Add the score from the break-triggering number in the column
                score += self.scoresheet[key][position]
        return score

    def calculate_total_score(self):
        self.total_score = sum(self.breaks)
