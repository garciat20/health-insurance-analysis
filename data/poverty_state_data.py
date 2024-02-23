"""
Purpose of this file is to parse specific data about poverty levels per state from the US Census Bureau API. -2020
"""

from config.api_config import POVERTY_URL, POVERTY_PARAMS
import requests

class PovertyStateData:
    __slots__ = ["data"]
    def __init__(self):
        response = requests.get(POVERTY_URL, params=POVERTY_PARAMS)
        self.data = response.json()

    def parsed_data_per_state(self):
        """
        Returns a dictionary containing every state code as the key and the values are the population used in the data collected along with the poverty rate
        """
        #The data returned from the API is all in strings, we have to convert to int

        states_data = {}