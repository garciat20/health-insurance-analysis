# health-insurance-analysis

## Description
Utilizing Python, I'll be gathering data from the US Census Bureau API concerning the amount of people insured/uninsured from the year 2020, and poverty levels from 2020 to illustrate a possible correlation between poverty levels and the number of uninsured people per state. I will use Plotly as the visualization tool to create choropleth maps, allowing for a clear and interactive representation of the data. This analysis aims to uncover any potential relationship between poverty rates and the lack of health insurance coverage across different states in the United States.

## Installation
```
pip install -r requirements.txt
```
or
```
pip3 install -r requirements.txt
```

## Usage
Once the requirments are installed you may run the primary file through the command line to showcase the visualizations via prompts given from the program. 
**NOTE:** The graphs made are not polished yet so they look a bit rough, and the data is from 2020 and I plan on somehow creating a time series analysis to see if the insurance coverage/ poverty per state correlation has been existent for a while.

```
python3 -m visualization.poverty_insurance_analysis
```

## TODO
- [ ] Time Series Analysis 
- [ ] Utilize ML Library To Predict Future Outcome
- [ ] Polish Visuals