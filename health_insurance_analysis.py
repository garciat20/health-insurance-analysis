"""
Purpose of this file to anaylze parsed data from the US Census Bureau API and visualize trends
between poverty and people insured in the United States (more specifcally the states).
"""

from insurance_state_data import InsuranceStateData
from poverty_state_data import PovertyStateData

class HealthInsuranceAnalysis:
    __slots__ = ["insurance_state_data", "poverty_state_data"]
    def __init__(self):
        self.insurance_state_data = InsuranceStateData().parsed_data_per_state() # dictionary of data returned
        self.poverty_state_data = PovertyStateData().parsed_data_per_state() # dictionary of data returned

    
