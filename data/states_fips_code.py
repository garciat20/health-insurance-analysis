"""
Helper to get the FIPS code for states
"""

import re

def parse_fips_file():
    """
    TODO: review code to see if works
    """
    keep_processing = False
    stop_processing = "county-level"

    state_code_andnames = {}

    with open("data/fips.txt") as f:
        for line in f:
            # elimniate all whitespace in a row
            columns = re.split('\s+', line.strip())

            # if multiple columns, combine the state names that have a space like "North Carolina"
            complete_state_name = ""

            # this is where i want to start iterating in the file
            if columns[0] == "-----------":
                keep_processing = True
                continue
                
            if columns[0] == stop_processing:
                break

            if keep_processing:
                if len(columns) > 2:
                    print(columns)
                    for i in range(1, len(columns)):
                        # combine the state names that have spaces
                        complete_state_name += columns[i] + " "
                    # strip any leading whitespace
                    complete_state_name = complete_state_name.strip()

                    # key is going to be the fips code and the value is going to be the state name
                    state_code_andnames[columns[0]] = complete_state_name

                elif len(columns) == 2:
                    # key is going to be the fips code and the value is going to be the state name
                    state_code_andnames[columns[0]] = columns[1]

    return state_code_andnames
            

print(parse_fips_file())