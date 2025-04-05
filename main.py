# import logging
# from flask import Flask, request, jsonify, render_template
# from backend.agents.understant_agent import UnderstandingAgent
# from backend.agents.research_agent import ResearchAgent
# from backend.agents.optimization_agent import OptimizationAgent
# from backend.agents.recommendation import RecommendationAgent

# app = Flask(__name__)

# API_KEY = "YOUR_API_KEY"

# # Configure logging
# logging.basicConfig(level=logging.DEBUG)

# @app.route('/')
# def index():
#     return render_template('index.html')

# @app.route('/get_flights', methods=['GET'])
# def get_flights():
#     try:
#         base_city = request.args.get('base_city')
#         destination = request.args.get('destination')
#         preference = request.args.get('preference')

#         app.logger.debug(f"Received request with base_city={base_city}, destination={destination}, preference={preference}")

#         travel_dates = ["2025-03-20", "2025-03-21"]

#         user_input = {
#             "base_city": base_city,
#             "destination": destination,
#             "dates": travel_dates,
#             "flexibility": 3,
#             "budget": 60000,
#             "group_type": "family"
#         }

#         understanding_agent = UnderstandingAgent(user_input)
#         parsed_input = understanding_agent.parse_input()

#         research_agent = ResearchAgent(API_KEY)
#         flight_data = research_agent.gather_flight_options(
#             parsed_input['base_city'], 
#             parsed_input['destination'], 
#             parsed_input['dates']
#         )

#         optimization_agent = OptimizationAgent(flight_data)
#         best_options = optimization_agent.find_best_options(preference)

#         recommendation_agent = RecommendationAgent(best_options)
#         recommendations = recommendation_agent.generate_recommendations()

#         # Ensure recommendations is a list of structured data
#         if not isinstance(recommendations, list):
#             recommendations = []

#         structured_recommendations = []
#         for rec in recommendations:
#             parts = rec.split(" | ")
#             structured_recommendations.append({
#                 "airline": parts[0],
#                 "price": parts[1],
#                 "duration": parts[2],
#                 "layovers": parts[3].replace("Layovers: ", "").strip("[]").split(", ")
#             })

#         app.logger.debug(f"Returning structured recommendations: {structured_recommendations}")
#         return jsonify(structured_recommendations)
#     except Exception as e:
#         app.logger.error(f"Error processing request: {e}")
#         return jsonify({"error": "An error occurred while processing your request."}), 500

# if __name__ == "__main__":
#     app.run(debug=True)

import logging
from flask import Flask, request, jsonify, render_template
from backend.agents.understant_agent import UnderstandingAgent
from backend.agents.research_agent import ResearchAgent
from backend.agents.optimization_agent import OptimizationAgent
from backend.agents.recommendation import RecommendationAgent

app = Flask(__name__)

API_KEY = "48f314181cmsh99c4ef645980101p13eb29jsn576e517b48e0"

# Configure logging
logging.basicConfig(level=logging.DEBUG)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_flights', methods=['GET'])
def get_flights():
    try:
        base_city = request.args.get('base_city')
        destination = request.args.get('destination')
        preference = request.args.get('preference')

        app.logger.debug(f"Received request with base_city={base_city}, destination={destination}, preference={preference}")

        travel_dates = ["2025-03-20", "2025-03-21"]

        user_input = {
            "base_city": base_city,
            "destination": destination,
            "dates": travel_dates,
            "flexibility": 3,
            "budget": 60000,
            "group_type": "family"
        }

        understanding_agent = UnderstandingAgent(user_input)
        parsed_input = understanding_agent.parse_input()

        research_agent = ResearchAgent(API_KEY)
        flight_data = research_agent.gather_flight_options(
            parsed_input['base_city'], 
            parsed_input['destination'], 
            parsed_input['dates']
        )

        optimization_agent = OptimizationAgent(flight_data)
        best_options = optimization_agent.find_best_options(preference)

        recommendation_agent = RecommendationAgent(best_options)
        recommendations = recommendation_agent.generate_recommendations()

        # Ensure recommendations is a list of structured data
        if not isinstance(recommendations, list):
            recommendations = []
            

        structured_recommendations = []
        for rec in recommendations:
            parts = rec.split(" | ")
            structured_recommendations.append({
                "airline": parts[0],
                "price": parts[1],
                "duration": parts[2],
                "layovers": parts[3].replace("Layovers: ", "").strip("[]").split(", ")
            })

        app.logger.debug(f"Returning structured recommendations: {structured_recommendations}")
        return jsonify(structured_recommendations)
    except Exception as e:
        app.logger.error(f"Error processing request: {e}")
        return jsonify({"error": "An error occurred while processing your request."}), 500

if __name__ == "__main__":
    app.run(debug=True)