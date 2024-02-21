"""
Purpose of this file is to store the API URL and parameters from the US Census Bureau API. 
"""
URL = "https://api.census.gov/data/timeseries/healthins/sahie"


params = {
    "get": "NIC_PT,NUI_PT,YEAR",
    "for": "county:*",
    "in": "state:*",
    "time": "2020",
    "key": "7f004ff88d81d41b6d2534a7ba93e3bd504a4521",
}