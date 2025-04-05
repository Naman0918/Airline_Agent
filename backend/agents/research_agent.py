class ResearchAgent:
    def __init__(self, api_key):
        self.api_key = api_key

    def gather_flight_options(self, base_city, destination, dates):
        sample_flight_data = [
            {
                "flight_number": "AI101",
                "airline": "Air India",
                "departure": "Mumbai",
                "arrival": "New York",
                "duration": "18h 30m",
                "price": 55000,
                "layovers": ["Delhi", "London"],
                "transit_time": "3h 15m"
            },
            {
                "flight_number": "EK501",
                "airline": "Emirates",
                "departure": "Mumbai",
                "arrival": "New York",
                "duration": "15h 0m",
                "price": 62000,
                "layovers": ["Dubai"],
                "transit_time": "1h 30m"
            },
            {
                "flight_number": "BA204",
                "airline": "British Airways",
                "departure": "Delhi",
                "arrival": "London",
                "duration": "9h 30m",
                "price": 45000,
                "layovers": ["Dubai", "Japan"],
                "transit_time": "4h 10m"
            }
        ]

        # # Debugging: Print flight data type
        # print(f"🔍 Data Type of `sample_flight_data`: {type(sample_flight_data)}")
        # print(f"🧩 First Element Type: {type(sample_flight_data[0])}")

        # Filter flights based on user's base city and destination
        filtered_flights = [
            flight for flight in sample_flight_data
            if isinstance(flight, dict)
            and flight['departure'].lower() == base_city.lower()
            and flight['arrival'].lower() == destination.lower()
        ]

        if not filtered_flights:
            print("\n❗ No flights found for the given route.")
        
        return filtered_flights

# import requests

# class ResearchAgent:
#     def __init__(self, api_key):
#         self.api_key = api_key

#     def gather_flight_options(self, base_city, base_city_id, destination, destination_id, date):
#         url = "https://skyscanner89.p.rapidapi.com/flights/one-way/list"
#         querystring = {
#             "origin": base_city,
#             "originId": base_city_id,
#             "destination": destination,
#             "destinationId": destination_id,
#             "date": date
#         }
#         headers = {
#             "x-rapidapi-key": self.api_key,
#             "x-rapidapi-host": "skyscanner89.p.rapidapi.com"
#         }

#         try:
#             response = requests.get(url, headers=headers, params=querystring)
#             response.raise_for_status()  # Raise an exception for HTTP errors
#             flight_data = response.json()

#             # Extract relevant flight information
#             filtered_flights = []
#             for flight in flight_data.get('flights', []):
#                 filtered_flights.append({
#                     "flight_number": flight.get("flight_number"),
#                     "airline": flight.get("airline"),
#                     "departure": flight.get("departure"),
#                     "arrival": flight.get("arrival"),
#                     "duration": flight.get("duration"),
#                     "price": flight.get("price"),
#                     "layovers": flight.get("layovers", []),
#                     "transit_time": flight.get("transit_time")
#                 })

#             return filtered_flights

#         except requests.exceptions.RequestException as e:
#             print(f"Error fetching flight data: {e}")
#             return []

# # Example usage
# if __name__ == "__main__":
#     agent = ResearchAgent("48f314181cmsh99c4ef645980101p13eb29jsn576e517b48e0")
#     flights = agent.gather_flight_options("NYCA", "27537542", "HNL", "95673827", "2025-03-20")
#     print(flights)