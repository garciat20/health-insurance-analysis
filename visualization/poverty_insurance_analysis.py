"""
Purpose of this file to anaylze parsed data from the US Census Bureau API and visualize trends
between poverty and people insured in the United States (more specifcally the states).
"""
import plotly.express as px

from data.insurance_state_data import InsuranceStateData
from data.poverty_state_data import PovertyStateData

class PovertyInsuranceAnalysis:
    __slots__ = ["insurance_state_data", "poverty_state_data"]
    def __init__(self):
        self.insurance_state_data = InsuranceStateData().parsed_data_per_state() # dictionary of data returned
        self.poverty_state_data = PovertyStateData().parsed_data_per_state() # dictionary of data returned

    def analyze_insurance_state_data(self):
        """
        Creates a visualization of the amount of people insured/ uninsured per state
        TODO: FIGURE OUT HOW TO ACTUALLY PLOT SOMETHING NOW, MAYBE USE HELPER FROM STATES_FIPS_CODE.PY
        """
        # we want a choropleth graph to graph the amount of people insured per state vs the population of the state

        fig = px.choropleth(locations=["CA", "TX", "NY"], locationmode="USA-states", color=[1,2,3], scope="usa")
        fig.show()


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
main()