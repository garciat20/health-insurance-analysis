"""
Purpose of this file to anaylze parsed data from the US Census Bureau API and visualize trends
between poverty and people insured in the United States (more specifcally the states).
"""
import plotly.express as px
import pandas as pd
import numpy as np

from data.insurance_state_data import InsuranceStateData
from data.poverty_state_data import PovertyStateData
from data.states_fips_code_and_name import parse_fips_file

STATE_ABBREVIATION = ["AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DC", "DE", "FL", "GA", "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD", "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ", "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC", "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"]

class PovertyInsuranceAnalysis:
    __slots__ = ["insurance_state_data", "poverty_state_data"]
    def __init__(self):
        self.insurance_state_data = InsuranceStateData() # dictionary of data returned
        self.poverty_state_data = PovertyStateData() # dictionary of data returned

    def analyze_insurance_state_data(self):
        """
        Creates a visualization of the amount of people insured/ uninsured per state
        TODO: FIGURE OUT HOW TO ACTUALLY PLOT SOMETHING NOW, MAYBE USE HELPER FROM STATES_FIPS_CODE.PY

        Notes from tutorial:
        - using examples from plotly data package it's evident we need data frames
        - not only that but we need to understand how the dataframe is setup
        - we can 

        What I understand so far:
        - I need to create a dataframe to use for the choropleth graph (with pandas)

        """

        # we want a choropleth graph to graph the amount of people insured per state vs the population of the state

        # lets make a dataframe to use for the choropleth graph (insured and uninsured people per state)

        #  below are simple examples of how to use pandas dataframes
        #  and how to query the dataframe!
        # ara1 = np.random.rand(5,2)
        # df1 = pd.DataFrame(ara1, columns=['A', 'B'])
        # queried = df1.query('A > 0.5 and B < 0.5')
        # print(df1)
        # print(queried)

        states_data = self.insurance_state_data.parsed_data_per_state()
        states_fips_code = [f'{fips:02}' for fips in states_data.keys()] # list of string of fips codes

        pop_nested_dict = states_data.values()

        # print(pop_nested_dict)

        df = pd.DataFrame(pop_nested_dict)
        # add column to datafram
        df.insert(0, "fips", states_fips_code)
        # df["fips"] = states_fips_code
        # dropped_df = df.drop(['uninsured_amt', 'population'], axis=1)
        print(df)
        """
        I want to show the states with the highest uninsured people, to do so I need to make the numbers
        of uninsured people proportional to the "population" (# of ppl that were surveryed to get this data)
        """


        fig = px.choropleth(
            data_frame=df, locations=STATE_ABBREVIATION,locationmode="USA-states", scope="usa", color="population",hover_name=STATE_ABBREVIATION, hover_data=["uninsured_amt", "insured_amt"],
            labels={"insured_amt": "Amount Of People Insured", "uninsured_amt": "Amount Of People Uninsured",
                    "population": "Number Of People Used For The Data"})
#   color_continuous_scale="Viridis", scope="usa"
            # labels={"insured_amt": "Amount Of People Insured", "uninsured_amt": "Amount Of People Uninsured",
            #         "population": "Number Of People Used For The Data"}
            # )
        fig.show()

        # color_num = [number for number in range(len(STATE_ABBREVIATION))]

        # data_frame_election = px.data.election()

        # print(px.data.election())
        
        # fig = px.bar(data_frame=data_frame_election,x="district",y="Coderre",labels={'x': 'District', 'y': 'total votes'})
        
        "to override, just use a dict in labels and set the x or y to the value you actually want to display as the label"
        # fig = px.bar(data_frame=data_frame_election, x="district", y="Coderre", labels={"Coderre": 'Votes For Coddere'})

        # Allows us to grab data from a supplied URL

        # fig = px.choropleth(data_frame=df,locations=STATE_ABBREVIATION, locationmode="USA-states", color=color_num, scope="usa")
        # fig.show()
        # return df


    def analyze_poverty_state_data():
        """
        Creates a visualizaiton of the amount of people insured/ uninsured per state
        """

    def anaylze_poverty_and_state_data():
        """
        Creates a visualzation based on poverty levels and people who have (or don't) insurance
        to draw a (possible) correlation between the two
        """

    def results():
        """
        TODO: May or may not actually implement this method ~ 
        """

def main():
    analysis = PovertyInsuranceAnalysis()
    analysis.analyze_insurance_state_data()

if __name__ == "__main__":
    main()
