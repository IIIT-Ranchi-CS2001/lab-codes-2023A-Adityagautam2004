import numpy as np
import pandas as pd

# Load the AQI data from the CSV file
aqi_data = pd.read_csv('AQI_Data.csv')

# Group the data by city and compute the mean of AQI, PM2.5, and PM10 values
city_aqi_mean = aqi_data.groupby('City')[['AQI', 'PM2.5', 'PM10']].mean()

# Use numpy to compute the mean of AQI, PM2.5, and PM10 values for each city
city_aqi_mean_numpy = np.mean(aqi_data[['AQI', 'PM2.5', 'PM10']].values, axis=0)

# Print the results
print("Mean AQI, PM2.5, and PM10 values for each city:")
print(city_aqi_mean)
print("\nMean AQI, PM2.5, and PM10 values using numpy:")
print(city_aqi_mean_numpy)