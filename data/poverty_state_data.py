"""
Purpose of this file is to parse specific data about poverty levels per state from the US Census Bureau API. -2020
"""

from config.api_config import POVERTY_URL, POVERTY_PARAMS
import requests
import pandas as pd

PERCENT_OF_PPL_IN_POV = "SAEPOVRTALL_PT"
STATE_ABREV = "STABREV"

class PovertyStateData:
    __slots__ = ["data"]
    def __init__(self):
        response = requests.get(POVERTY_URL, params=POVERTY_PARAMS)
        self.data = response.json()

    def parsed_data_per_state(self):
        """
        Returns a dataframe of the data going to be plotted, this API ate 🐥
        """
        # API provided me a lot of good things yessss

        df = pd.DataFrame(self.data)

        # rename() returns a df, so we can just say "manipulate the og one and leave as is"
        df = df.rename(columns={0: "SAEPOVRTALL_PT", 1: "STABREV", 2: "YEAR", 3: "state"})

        # we want everything except the header, and adjust indices that were possibly modified
        df = df.iloc[1:].reset_index(drop=True)

        # change 1st column to numeric type (float)
        df["SAEPOVRTALL_PT"] = df["SAEPOVRTALL_PT"].apply(pd.to_numeric)
        

        # "TODO: MAYBE ADD BACK YEAR COLUMN INCASE IF DO A TIME SERIES ANALYSIS"
        # we want to remove the last column, as its not needed 
        df = df.iloc[:, :-1]

        return df



def main():
    psd = PovertyStateData()
    print(psd.parsed_data_per_state())

if __name__ == "__main__":
    main()