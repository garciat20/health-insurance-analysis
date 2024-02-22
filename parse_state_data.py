import requests
import matplotlib.pyplot as plt
from api_config import URL, params

"""
Purpose of this file is to analyze the health insurance data from the US Census Bureau API.
"""
UNINSURED_AMT_OF_PPL = "uninsured_amt"
INSURED_AMT_OF_PPL = "insured_amt"
POP_FROM_STATE = "population"

class ParseStateData:
    __slots__ = ["data"]

    def __init__(self):
        response = requests.get(URL, params=params)
        self.data = response.json()
        
    def parse_data_per_state(self):
        """
        Returns a dictionary containing every state code as the key and the values are the population used in the data collected along with uninsured/ insured people
        """
        #The data returned from the API is all in strings, we have to convert to int

        states_data = {} # store's data corresponding to a state's code

        # lets add up each state's population from the information given from the countiess
        state_code = -1
        county_code = -1

        state_col = 4
        county_col = 5
        insured_col = 0
        uninsured_col = 1

        # skip header
        for row in self.data[1:]:

            # firstly, we want to avoid dealing with null values so we'll skip that row
            if (self.is_valid_data(row[insured_col], row[uninsured_col]) == False):
                continue

            # if current statecode doesn't match previous one, that means we hit a new state because our data is organized in ascending order
            curr_state_code = int(row[state_col])
            curr_county_code = int(row[county_col])
            if (curr_state_code != state_code):
                state_code = curr_state_code
                county_code = curr_state_code

                # create a nested dict for a state that contains many values! the state code will be the key
                states_data[state_code] = {INSURED_AMT_OF_PPL: 0, UNINSURED_AMT_OF_PPL: 0, POP_FROM_STATE: 0}

            # check the state code and county code of new row matches criteria to add up a state's population
            if (curr_state_code == state_code and curr_county_code != county_code):
                # county col shouldn't match county code so no duplicates in population addition

                # get nested dict from state code:
                pop_val_dict = states_data[state_code] # nested dict

                # add the population of the uninsured/ insured people of different counties of the same state
                insured_pop = int(row[insured_col])
                uninsured_pop = int(row[uninsured_col])

                # loop thru nested dict
                for key, val in pop_val_dict.items():
                    if key == UNINSURED_AMT_OF_PPL:
                        pop_val_dict[key] = val + uninsured_pop  #update uninsured pop accordingly
                    if key == INSURED_AMT_OF_PPL:
                        pop_val_dict[key] = val + insured_pop   #update insured pop accordingly
                    if key == POP_FROM_STATE:
                        pop_val_dict[key] = val + insured_pop + uninsured_pop

        return states_data
    
    def is_valid_data(self, insured_pop, uninsured_pop):
        """
        If there's a piece of data that is 'null' we will avoid that row.
        """
        if (insured_pop == None or uninsured_pop == None):
            return False
        return True


def main():
    state_data = ParseStateData()
    parsed_data = state_data.parse_data_per_state()
    print(parsed_data)

main()
