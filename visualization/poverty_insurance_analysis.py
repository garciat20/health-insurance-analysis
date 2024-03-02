"""
Purpose of this file to anaylze parsed data from the US Census Bureau API and visualize trends
between poverty and people insured in the United States (more specifcally the states).
"""
import plotly.express as px
import pandas as pd

from data.insurance_state_data import InsuranceStateData
from data.poverty_state_data import PovertyStateData
from data.states_fips_code_and_name import get_fips_in_seq_order, get_state_names_by_fips_order

STATE_ABBREVIATION = ["AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DC", "DE", "FL", "GA", "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD", "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ", "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC", "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"]

INSURED_VS_POP_COLUMN = "uninsured_vs_state_pop"

PERCENT_OF_PPL_IN_POV_COLUMN = "SAEPOVRTALL_PT"
STATE_ABREV_COLUMN = "STABREV"

PROMPT = """
Which analysis would you like to see?
1. Percentage of Uninsured Population by State - 2020
2. Percentage of People in Poverty by State - 2020 
3. Trend between Poverty and Uninsured People by State - 2020 (NOT DONE)
Enter a number corresponding to the analysis you'd like to see: """

class PovertyInsuranceAnalysis:
    __slots__ = ["insurance_state_data", "poverty_state_data", "state_names"]
    def __init__(self):
        self.insurance_state_data = InsuranceStateData() # dictionary of data returned
        self.poverty_state_data = PovertyStateData() # dictionary of data returned
        self.state_names = get_state_names_by_fips_order()

    def analyze_insurance_state_data(self):
        """
        Creates a visualization of the percentage of uninsured people per state
        TODO: make numbers look prettier somehow when you hover over the state
        """
        # using helper function to get fips codes per state and converting to list
        states_data = self.insurance_state_data.parsed_data_per_state()
        states_fips_code = [f'{fips:02}' for fips in states_data.keys()] # list of string of fips codes

        # lets get nested dict that contains amt_insured, amt_uninsured, pop_per_state
        pop_nested_dict = states_data.values()

        # everything is organized in order by FIPS code so it makes it easier, i can just enter the data raw

        proportional_uninsured_results = self.insurance_state_data.proportion_of_uninsured_to_state_pop()

        df = pd.DataFrame(pop_nested_dict)
        # add column to datafram
        df.insert(0, "fips", states_fips_code)
        df.insert(1, "state_name", STATE_ABBREVIATION)
        df.insert(2, "uninsured_vs_state_pop", proportional_uninsured_results)
        # columns are fips, state_name, uninsured..., insured_amt, uninsured_amt, population --> maybe missing one? somehow check later

        # i did hover_data as such since I don't know how else to remove locations from being shown when hovering over a state
        # idk, i just used the dataframe for locations, i used the constant above but there were issues and I couldn't hide it
        # using the dataframe helped avoid this issue, why it happned? idk, it said UNHASHABLE Type and i tried to set the constant
        # to false in the hover_data dict
        fig = px.choropleth(
            # locations, using dataframe column 'state_name' it somehow understands that idk, color highlights the important part
            data_frame=df, locations="state_name",locationmode="USA-states", scope="usa",color=INSURED_VS_POP_COLUMN,
            color_continuous_scale="RdBu",
            title="Percentage of Uninsured Population by State - 2020",
            # when i hover i want to emphasize something/ make it bold (hover_name)
            # i want to display certain data when i hover over something (hover_data)
            hover_name=self.state_names, hover_data={'state_name': False,"uninsured_amt": True, "insured_amt": True, "population": True, INSURED_VS_POP_COLUMN: True},
            # rename columns to something more meaningful
            labels={"insured_amt": "Amount Of People Insured", "uninsured_amt": "Amount Of People Uninsured",
                    "population": "Number Of People Used For The Data",
                    INSURED_VS_POP_COLUMN: "Percentage Of State Uninsured",
                    })

        fig.show()

    def analyze_poverty_state_data(self):
        """
        Creates a visualization of the percentage of people in poverty per state
        TODO: make numbers look prettier somehow when you hover over the state
        TODO: Somehow the colorbar isn't in the graph, I don't know why, I'll have to look into it: SOLVED
        FORGOT TO CHANGE TYPE IN PANDAS COLUMN
        """
        df = self.poverty_state_data.parsed_data_per_state()
       
        fig = px.choropleth(
            data_frame=df,locations=STATE_ABREV_COLUMN,locationmode="USA-states",scope="usa",
            color=PERCENT_OF_PPL_IN_POV_COLUMN,
            color_continuous_scale="Viridis",
            hover_name=self.state_names,
            hover_data={STATE_ABREV_COLUMN: False},
            labels={PERCENT_OF_PPL_IN_POV_COLUMN: "Percentage Of State In Poverty"},
            title="Percentage of Poverty Population by State - 2020"
        )

        fig.show()

    def anaylze_poverty_and_uninsured_data():
        """
        Creates a visualzation based on poverty levels and people who have (or don't) insurance
        to draw a (possible) correlation between the two
        """
        print('no')


def main():
    """
    Prompts user as to which visualization they would like to see.
    """
    user_selection = int(input(PROMPT))
    analysis = PovertyInsuranceAnalysis()

    # percentage of uninsured people per state
    if user_selection == 1:
        analysis.analyze_insurance_state_data()
    
    # percentage of people in poverty per state
    elif user_selection == 2:
        analysis.analyze_poverty_state_data()

    # combine results to draw a correlation
    elif user_selection == 3:
        analysis.analyze_insurance_state_data()

if __name__ == "__main__":
    main()
