import pandas as pd
import ssl
import urllib.request

# For this exercise we will focus on one data set from the City of New York
# For expanding this topic I recommend working with multiple data sourcing and engaging in some good old fashion ETL
# The caveat is that all data sources available differ vastly from one another. The metadata is very different hence the ETL exercise recommendation if you are doing a large project

# Bypass SSL verification by creating an unverified SSL context
ssl_context = ssl._create_unverified_context()

# URL of the dataset
# This variable can be a list if you are using multiple data sources. Keep in mind that for the sake of simplicity we stuck to one data source.
url = "https://data.cityofnewyork.us/resource/h9gi-nx95.csv?$limit=50000"

# Open the URL with the unverified SSL context
with urllib.request.urlopen(url, context=ssl_context) as response:
    # Read the dataset into a Pandas DataFrame
    df = pd.read_csv(response)

# Perform some Data Cleaning
df = df.dropna(subset=['latitude', 'longitude'])  # Remove rows without location data to have a neater resulting set
df['date'] = pd.to_datetime(df['crash_date'])  # Convert dates to datetime format and handle those datetime data types. They can be messy if left unhandled
df['time'] = pd.to_datetime(df['crash_time'], format='%H:%M').dt.time

# Tell your query to focus on relevant columns
df = df[['date', 'time', 'latitude', 'longitude', 'number_of_persons_injured',
         'number_of_persons_killed', 'contributing_factor_vehicle_1']]

# And proceed to save cleaned data
# The file nyc_traffic_bottlenecks_cleaned.csv will be saved in the same directory as your python scripts
df.to_csv("./TrafficBottleNecksAccidentsNY/nyc_traffic_bottlenecks_cleaned.csv", index=False)
print("Dataset saved as 'nyc_traffic_bottlenecks_cleaned.csv'")
