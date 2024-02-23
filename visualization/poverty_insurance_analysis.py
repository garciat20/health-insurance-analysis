"""
Purpose of this file to anaylze parsed data from the US Census Bureau API and visualize trends
between poverty and people insured in the United States (more specifcally the states).
"""
import plotly.express as px
import pandas as pd

from data.insurance_state_data import InsuranceStateData
from data.poverty_state_data import PovertyStateData
from data.states_fips_code_and_name import parse_fips_file, get_state_names_by_fips_order

STATE_ABBREVIATION = ["AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DC", "DE", "FL", "GA", "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD", "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ", "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC", "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"]

INSURED_VS_POP_COLUMN = "uninsured_vs_state_pop"


class PovertyInsuranceAnalysis:
    __slots__ = ["insurance_state_data", "poverty_state_data"]
    def __init__(self):
        self.insurance_state_data = InsuranceStateData() # dictionary of data returned
        self.poverty_state_data = PovertyStateData() # dictionary of data returned

    def analyze_insurance_state_data(self):
        """
        Creates a visualization of the percentage of uninsured people in a state
        TODO: make numbers look prettier somehow when you hover over the state
        """
        # using helper function to get fips codes per state and converting to list
        states_data = self.insurance_state_data.parsed_data_per_state()
        states_fips_code = [f'{fips:02}' for fips in states_data.keys()] # list of string of fips codes

        # lets get nested dict that contains amt_insured, amt_uninsured, pop_per_state
        pop_nested_dict = states_data.values()

        # everything is organized in order by FIPS code so it makes it easier, i can just enter the data raw
        state_name_list = get_state_names_by_fips_order()

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
            title="Percentage of Uninsured Population by State - 2020",
            # when i hover i want to emphasize something/ make it bold (hover_name)
            # i want to display certain data when i hover over something (hover_data)
            hover_name=state_name_list, hover_data={'state_name': False,"uninsured_amt": True, "insured_amt": True, "population": True, INSURED_VS_POP_COLUMN: True},
            # rename columns to something more meaningful
            labels={"insured_amt": "Amount Of People Insured", "uninsured_amt": "Amount Of People Uninsured",
                    "population": "Number Of People Used For The Data",
                    INSURED_VS_POP_COLUMN: "Percentage Of State Uninsured",
                    })

        fig.show()



    def analyze_poverty_state_data():
        """
        Creates a visualizaiton of the amount of people insured/ uninsured per state
        """

    def anaylze_poverty_and_uninsured_data():
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
