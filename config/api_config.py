"""
Purpose of this file is to store the API URL and parameters from the US Census Bureau API. 
"""

HEALTH_INSURANCE_URL = "https://api.census.gov/data/timeseries/healthins/sahie?"
POVERTY_URL = "https://api.census.gov/data/timeseries/poverty/saipe?"
KEY = "7f004ff88d81d41b6d2534a7ba93e3bd504a4521"


HEALTH_INSURANCE_PARAMAS = {
    "get": "NIC_PT,NUI_PT,YEAR",
    "for": "county:*",
    "in": "state:*",
    "time": "2020",
    "key": KEY,
}

POVERTY_PARAMS = {
    "get" : "SAEPOVRTALL_PT,STABREV",
    "YEAR": 2020,
    "for": "state:*",
    "key": KEY
}