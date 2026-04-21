from pytrends.request import TrendReq
import pandas as pd

pytrends = TrendReq(hl='en-US', tz=330)

keywords = ["AI jobs", "data science", "machine learning"]

pytrends.build_payload(keywords, timeframe='today 12-m')

data = pytrends.interest_over_time()

data.to_csv("data/sample_data.csv")

print("Data collected successfully!")
