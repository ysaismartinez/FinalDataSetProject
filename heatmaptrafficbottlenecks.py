import folium
from folium.plugins import HeatMap
import pandas as pd
from sklearn.cluster import DBSCAN
import numpy as np

# After we have a clean proprocessed generated data 
# Let's load cleaned dataset
# We will prepare things to generate to data analysis, some visualizations, and generate the geojason dataset
data = pd.read_csv("./TrafficBottleNecksAccidentsNY/nyc_traffic_bottlenecks_cleaned.csv")

# Let's create a base map
map_nyc = folium.Map(location=[40.7128, -74.0060], zoom_start=12)

# and add heatmap
heat_data = data[['latitude', 'longitude']].dropna().values.tolist()
HeatMap(heat_data, radius=10).add_to(map_nyc)

# We will save the map as HTML and we will use this html to do the visualization. I got mixed results depending on where I ran this from. It had issues rendering when running from VS Code (My preferred IDE)
map_nyc.save("./HeatMapandGeoJsonDataset/nyc_traffic_bottlenecks_heatmap.html")
# This is just a print to let the user know that we saved the heatmap as HTML
print("Heatmap saved as 'nyc_traffic_bottlenecks_heatmap.html'")

# Now let's do some basic statistics
print("Summary Statistics:")
print(data.describe())

# and print the output of the describe() method with the header: Top Contributing Factors
print("\nTop Contributing Factors:")
print(data['contributing_factor_vehicle_1'].value_counts().head(10))

# We are ready to prepare data for clustering
coords = data[['latitude', 'longitude']].dropna().to_numpy()
db = DBSCAN(eps=0.01, min_samples=5).fit(coords)

# First let's add cluster labels to dataset
data['cluster'] = db.labels_

# Then let's visualize clusters
import matplotlib.pyplot as plt
plt.scatter(data['longitude'], data['latitude'], c=data['cluster'], cmap='viridis', s=1)
plt.title('Traffic Bottleneck Clusters')
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.show()

# Save dataset in GeoJSON format for sharing
import geopandas as gpd
from shapely.geometry import Point

# and finally create GeoDataFrame
gdf = gpd.GeoDataFrame(data, geometry=gpd.points_from_xy(data.longitude, data.latitude))
gdf.to_file("./HeatMapandGeoJsonDataset/nyc_traffic_bottlenecks.geojson", driver="GeoJSON")
print("Dataset saved as 'nyc_traffic_bottlenecks.geojson'")

