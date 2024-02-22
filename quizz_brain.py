class QuizzBrain:
    def __init__(self, statesList):
        self.statesList = statesList
        self.score = 0
        self.total_states = 50
        self.found_states = []

    def check_answer(self, answer):
        for state_data in self.statesList:
            if answer.lower() in self.found_states:
                return "Already Found!"
            if answer.lower() == state_data["state"].lower():
                self.score += 1
                self.statesList.remove(state_data)
                self.found_states.append(state_data["state"].lower())
                return True, self.get_state_coordinates(
                    state_data["state"], state_data["x"], state_data["y"]
                )
        return False

    def ask_user_input(self, user_answer):
        if user_answer == "exit":
            self.end_game()
            return False
        return self.check_answer(user_answer)

    def display_score(self):
        return f"{self.score} / {self.total_states}"

    def is_there_more_states(self):
        return self.score < self.total_states

    def get_state_coordinates(self, state_name, x, y):
        return {"name": state_name, "x": x, "y": y}

    def get_score(self):
        return self.score

    def end_game(self):
        self.display_score()
        return
