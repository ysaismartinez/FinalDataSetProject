import unittest
from unittest.mock import patch, MagicMock
import os
import pandas as pd
import numpy as np

#Below is a simple unit test to make sure the key outouts from the heatmap script work as expected. 
class TestTrafficBottlenecksScript(unittest.TestCase):
    @patch('folium.Map.save')
    @patch('pandas.read_csv')
    @patch('geopandas.GeoDataFrame.to_file')
    def test_script_execution(self, mock_to_file, mock_read_csv, mock_save):

        # Mock the dataset to avoid file I/O
        mock_data = pd.DataFrame({
            'latitude': [40.7128, 40.7138, 40.7148],
            'longitude': [-74.0060, -74.0070, -74.0080],
            'contributing_factor_vehicle_1': ['Factor1', 'Factor2', 'Factor1']
        })
        mock_read_csv.return_value = mock_data

        # Mock saving methods to avoid file creation
        # This won't have us creating new files that we do not need
        mock_save.return_value = None
        mock_to_file.return_value = None

        # Import the script 
        # This is simply pulling from the script I created
        import heatmaptrafficbottlenecks

        # Assertions to check key operations
        # We will if files were saved and operations were completed
        # Check if the heatmap HTML was "saved"
        mock_save.assert_called_once_with("./HeatMapandGeoJsonDataset/nyc_traffic_bottlenecks_heatmap.html")
        
        # Check if the GeoJSON was "saved"
        mock_to_file.assert_called_once_with("./HeatMapandGeoJsonDataset/nyc_traffic_bottlenecks.geojson", driver="GeoJSON")

        # Check if DBSCAN labels were added
        self.assertIn('cluster', mock_data.columns)
        self.assertTrue(np.issubdtype(mock_data['cluster'].dtype, np.integer))

        # Check if top contributing factors are calculated
        top_factors = mock_data['contributing_factor_vehicle_1'].value_counts().head(10)
        self.assertGreater(len(top_factors), 0)

#Let's run the test! 
if __name__ == '__main__':
    unittest.main()
