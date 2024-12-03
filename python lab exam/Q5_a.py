import pandas as pd

data = pd.read_csv("AQI_Data.csv")

average_aqi_by_city = data.groupby('City')['AQI'].mean()

print("Average AQI by City:\n", average_aqi_by_city)