import pandas as pd

# Load the AQI data from the CSV file
aqi_data = pd.read_csv('AQI_Data.csv')

# Group the data by City and calculate the maximum PM10 level for each city
max_pm10_by_city = aqi_data.groupby('City')['PM10'].max().reset_index()

# Print the result
print(max_pm10_by_city)