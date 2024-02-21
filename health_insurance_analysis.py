import requests
import matplotlib.pyplot as plt
from api_config import URL, params

"""
Purpose of this file is to analyze the health insurance data from the US Census Bureau API.
"""

class HealthInsuranceAnalysis:
    __slots__ = ["data"]

    def __init__(self):
        response = requests.get(URL, params=params)
        self.data = response.json()
        


    # poverty_rates = []

    # state_code = []
    # theres also county code but thats later

    # NIC_PT, NUI_PT, YEAR

    # value_identity = ["NIC_PT", "NUI_PT"]

    # # skip column headers in first row
    # for row in data[1:]:
    #     # don't care about data that has a null in it 
    #     if (row[0] == None or row[1] == None):
    #         continue
    #     insured.append(int(row[0]))
    #     uninsured.append(int(row[1]))
    #     state_code.append(int(row[4]))

    """
    REWRITE CODE TO MAKE IT TAKE RETURN LIST OF DICTIONARIES OF A STATE'S INFO
    TODO: rewrite code, figure out how to make a dictionary with 3 key value pairs to then append to a list
    TODO: check the first for loop and see if the code makes sense, write it out

    """
    "population here means, the amount of people surveryed to get this data"
    def pop_calulation_per_state(self):
        "The data returned from the API is all in strings, we have to convert to int"


        amt_of_insured_ppl = []
        amt_of_uninsured_ppl = []

        # store state codes and the corresponding population
        all_states_data = [] # use this to store all the data relating to a state 
        state_dicts = {}

        # lets add up each state's population from the information given from the countiess
        state_code = -1
        county_code = -1

        state_col = 4
        county_col = 5
        insured_col = 0
        uninsured_col = 1

        for row in self.data[1:]:

            # firstly, we want to avoid dealing with null values so we'll skip that row
            if (self.is_valid_data(row[insured_col], row[uninsured_col]) == False):
                continue

            # if current statecode doesn't match previous one, that means we hit a new state because our data is organized in ascending order
            # for the state codes
            curr_state_code = int(row[state_col])
            curr_county_code = int(row[county_col])
            if (curr_state_code != state_code):
                state_code = curr_state_code
                county_code = curr_state_code

                # create a new dictionary with the statecode and the corresponding population
                # dummy value is 0 since this if statement creates a new state to find the pop of
                state_dicts[state_code] = 0
                state_dicts["insured amount"] = 0
                state_dicts["uninsured amount"] = 0

                all_states_data.append(state_dicts) # one list contains a dictionary of info for a state
                

            # check the state code and county code of new row matches criteria to add up a state's population
            if (curr_state_code == state_code and curr_county_code != county_code):
                # county col shouldn't match county code so no duplicates in population addition

                pop_val = state_dicts[state_code] # get current population 
                insuranced_amount = state_dicts["insured amount"]
                uninsured_amount = state_dicts["uninsured amount"]

                # add the population of the uninsured/ insured people of different counties of the same state
                insured_pop = int(row[insured_col])
                uninsured_pop = int(row[uninsured_col])

                pop_val += (insured_pop + uninsured_pop) # update current population
                insuranced_amount += insured_pop # update current insured amount of people
                uninsured_amount += uninsured_pop # update current uninsured amount of people

                #update dict population, insured, and uninsured amount
                state_dicts[state_code] = pop_val
                state_dicts["insured amount"] = insuranced_amount
                state_dicts["uninsured amount"] = uninsured_amount

        return all_states_data
    
    def is_valid_data(self, insured_pop, uninsured_pop):
        if (insured_pop == None or uninsured_pop == None):
            return False
        return True


def main():
    health_insurance = HealthInsuranceAnalysis()
    state_pop = health_insurance.pop_calulation_per_state()
    print(state_pop)

main()
# # print (uninsured)
# # print (insured)

# # want to get total amount of people surveryed from data so its insured + uninsured
# # assuming both lists are the same length
# total_population_per_state = []

# for i in range(len(uninsured)):
    
#     total_population_per_state.append(uninsured[i] + insured[i])

# for i in range(len(total_population_per_state)):
#     print(f"state {i" )

# Create horizontal bar graph
# plt.figure(figsize=(7, 5))

# plot multiple bars, one bar for insured people and one bar for uninsured people
# the y axis will the min population to the max population

# x-axis is the insured and uninsured people bars

# plt.bar(value_identity,)
