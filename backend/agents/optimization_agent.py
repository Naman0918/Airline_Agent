# class OptimizationAgent:
#     def __init__(self, flight_data):
#         self.flight_data = flight_data

#     def find_best_options(self, sorting_preference="price"):  # Added `sorting_preference` parameter
#         if sorting_preference == "price":
#             sorted_flights = sorted(
#                 self.flight_data,
#                 key=lambda x: x['price']
#             )
#         elif sorting_preference == "duration":
#             # Assuming 'duration' format is "18h 20m" → Convert to minutes for sorting
#             sorted_flights = sorted(
#                 self.flight_data,
#                 key=lambda x: int(x['duration'].split('h')[0]) * 60 + int(x['duration'].split(' ')[1].replace('m', ''))
#             )
#         else:
#             sorted_flights = sorted(self.flight_data, key=lambda x: x['price'])
        
#         return sorted_flights[:3]  

class OptimizationAgent:
    def __init__(self, flight_data):
        self.flight_data = flight_data

    def find_best_options(self, sorting_preference):
        if sorting_preference == "1":
            sorted_flights = sorted(self.flight_data, key=lambda x: x['price'])
        elif sorting_preference == "2":
            sorted_flights = sorted(self.flight_data, key=lambda x: int(x['duration'].split('h')[0]))
        else:
            print("\n❗ Invalid choice. Showing default (Cheapest first).")
            sorted_flights = sorted(self.flight_data, key=lambda x: x['price'])

        return sorted_flights[:3]  
# class OptimizationAgent:
#     def __init__(self, flight_data):
#         self.flight_data = flight_data

#     def find_best_options(self, preference):
#         if preference == "1":  # Sort by price (Cheapest first)
#             sorted_flights = sorted(self.flight_data, key=lambda x: x['price'])
#         elif preference == "2":  # Sort by duration (Fastest first)
#             sorted_flights = sorted(self.flight_data, key=lambda x: x['duration'])
#         else:
#             sorted_flights = self.flight_data

#         return sorted_flights[:3]  # Return top 3 options