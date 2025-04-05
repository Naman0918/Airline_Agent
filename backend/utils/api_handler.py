import requests
import json

class APIHandler:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "https://api.skyscanner.net/apiservices"

    def get_flight_data(self, origin, destination, date):
        endpoint = f"{self.base_url}/browsequotes/v1.0/IN/INR/en-US/{origin}/{destination}/{date}"
        headers = {"apikey": self.api_key}
        response = requests.get(endpoint, headers=headers)
        if response.status_code == 200:
            return response.json()
        else:
            return {"error": "Unable to fetch data"}
