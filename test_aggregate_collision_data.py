import unittest
from unittest.mock import patch, MagicMock
from io import BytesIO
import pandas as pd
import urllib.request

class TestNYCTrafficBottlenecks(unittest.TestCase):

    @patch('urllib.request.urlopen')
    def test_data_processing(self, mock_urlopen):
        # Mock the dataset (BytesIO for file-like object)
        # We will pass on the fields and the mock attributes value.
        mock_data = BytesIO(b"""
crash_date,crash_time,latitude,longitude,number_of_persons_injured,number_of_persons_killed,contributing_factor_vehicle_1
2024-01-01,12:00,40.7128,-74.0060,2,0,Driver Inattention
2024-01-02,15:30,40.7129,-74.0059,1,1,Speeding
""")
        mock_urlopen.return_value = mock_data

        # Recreate the script logic
        # The resulting data will be read as a CSV from the pandas object below
        # In all our scripts we are bypassing the SSL verification to keep things simple but this should never be done in production

        url = "https://data.cityofnewyork.us/resource/h9gi-nx95.csv?$limit=50000"
        ssl_context = MagicMock()

        with urllib.request.urlopen(url, context=ssl_context) as response:
            # Ensure pandas reads the CSV correctly
            df = pd.read_csv(response)

        # Let's do some data Cleaning
        df = df.dropna(subset=['latitude', 'longitude'])
        df['date'] = pd.to_datetime(df['crash_date']) # and let's properly handle the date/time data objects. They can get messy if left unaddressed.\
        df['time'] = pd.to_datetime(df['crash_time'], format='%H:%M').dt.time

        # Focus on relevant columns
        df = df[['date', 'time', 'latitude', 'longitude', 'number_of_persons_injured',
                 'number_of_persons_killed', 'contributing_factor_vehicle_1']]

        # Proceed to validate DataFrame shape
        self.assertEqual(len(df), 2)  # Two rows in the mock data
        self.assertEqual(list(df.columns), ['date', 'time', 'latitude', 'longitude',
                                            'number_of_persons_injured', 'number_of_persons_killed',
                                            'contributing_factor_vehicle_1'])

        # Proceed to validate specific data
        self.assertEqual(df.iloc[0]['latitude'], 40.7128)
        self.assertEqual(df.iloc[1]['contributing_factor_vehicle_1'], 'Speeding')

# Run the unit test
if __name__ == "__main__":
    unittest.main(exit=False)
