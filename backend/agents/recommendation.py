class RecommendationAgent:
    def __init__(self, best_options):
        self.best_options = best_options

    def generate_recommendations(self):
        recommendations = []
        for flight in self.best_options:
            rec = (
                f"{flight['airline']} | ₹{flight['price']} | "
                f"Duration: {flight['duration']} | "
                f"Layovers: {flight['layovers']} | "
                # f"Convenience Score: {flight['convenience_score']}"
            )
            recommendations.append(rec)
        return recommendations
