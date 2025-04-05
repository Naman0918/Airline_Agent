class UnderstandingAgent:
    def __init__(self, user_input):
        self.input_data = user_input

    def parse_input(self):
        return {
            "base_city": self.input_data.get("base_city"),
            "destination": self.input_data.get("destination"),
            "dates": self.input_data.get("dates"),
            "flexibility": self.input_data.get("flexibility"),
            "budget": self.input_data.get("budget"),
            "group_type": self.input_data.get("group_type"),
        }
