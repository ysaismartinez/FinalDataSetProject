Requirements:

1: Description of problem/motivation you are solving with this dataset

    Traffic Bottlenecks:

    What are they? Traffic bottlenecks are recurring points of congestion that result in delays, increased fuel consumption, and frustration for commuters.
    Why is this topic important? Identifying and understanding these bottlenecks is critical for urban planning, traffic management, and improving road efficiency.
    How will I address this problem in this assignment? By analyzing spatial and temporal traffic data, we can pinpoint problem areas, uncover underlying causes, and propose data-driven solutions such as signal adjustments, lane expansions, or alternative routing.
    
    There are three main motivating factors for me:
        Economic Impact: Reduced productivity due to delays.
        Environmental Concerns: Increased emissions from idling vehicles.
        Safety: Bottlenecks often contribute to accidents and emergency response delays.

2: Review of previous datasets in the domain of interest (if any) and how your dataset is novel

    Every research I did online using Google, Bing, and SearchGPT pointed me to datasets from very large urban areas like LA and NYC. Uber, Google Maps, and Tesla also have rich data sets available.

    METR-LA: Focuses on traffic prediction using speed and volume data across LA's road network. Limited insights into bottlenecks as it emphasizes real-time trends.

    Traffic4cast: City-wide traffic density data, suitable for visualizing congestion patterns but lacks granularity in causative factors.

    NYC Vision Zero Data: Rich in accident and traffic violation data but doesn't directly highlight persistent congestion areas.

    Novelty of Dataset: This dataset combines static traffic flow data, incident reports, and spatial data to specifically target recurring bottlenecks. It incorporates:
        Multi-source integration (e.g., accidents, sensor data, road closures).
        Focus on location-specific congestion, not time-sensitive predictions.
        Insights into causative factors (e.g., infrastructure issues, accidents, peak-hour flow).

3: Power analysis to determine amount of data needed

    Metric: Use the coefficient of variation (CV) in traffic speed/flow across multiple locations to identify variability.
    Required Data Points:
        Spatial Distribution: Cover 10–20 significant road segments per city/region.
        Temporal Coverage: At least 3–6 months of data to capture weekday, weekend, and seasonal patterns.
        Data Size: Estimated 5–10 million data points (1,000 data points/day/location over 6 months).

4: Tool(s) to source data (web scraping tool, tool for labeling images, web app to collect user data, surveys, firmware logging for a sensor, mobile app to collect data from phone/watch sensors, etc)

    Data Sources:
        OpenStreetMap: For road networks and infrastructure data.
        NYC Open Data/Caltrans PeMS: Traffic flow, sensor data, and incident reports.
        Google Maps/HERE API: Supplementary real-time flow and incidents.
    Python Tools:
        osmnx: For fetching and visualizing road networks.
        requests: To interact with APIs.
        pandas/geopandas: For preprocessing and spatial analysis.
        folium/matplotlib: For visualization of bottlenecks.

5: Exploratory data analysis of dataset

    Spatial Patterns: Visualize bottleneck locations on a map.
    Temporal Trends: Analyze congestion by time of day, day of week, and season.

    Root Causes:
        Correlate incidents (e.g., accidents, roadwork) with congestion patterns.
        Analyze lane counts, signal timings, and alternative routes.

    Techniques:
        Heatmaps: Show areas with the highest congestion frequency.
        Cluster Analysis: Identify groups of nearby bottlenecks.
        Descriptive Statistics: Average speed, volume, and delays per location.

6: Ethics statement

    1. Privacy: Ensure anonymization of data, especially when using GPS or user-sourced data.
    2. Equity: Ensure bottleneck solutions do not disproportionately favor certain demographics or areas (e.g., affluent neighborhoods, mostly white/black/Hispanic, etc.).
    3. Transparency: Document data sources and preprocessing methods to enable reproducibility.

7: Open source license 

    Apache 2 License. The entire license can be found here: https://www.apache.org/licenses/LICENSE-2.0 

8: Open source dataset via one of the following: Hugging Face Datasets Hub (free), Kaggle (free), AWS Open Datasets (free for 2 years after review), hosting yourself ($)

    To satisfy this assignment I hosted the dataset here: https://huggingface.co/datasets/ysaismartinez/TrafficBottleNecksAccidentsNY/tree/main
    However, it is also in GitHub which has all the other artifacts of my project: https://github.com/ysaismartinez/FinalDataSetProject/tree/FinalDataSetBranch/HeatMapandGeoJsonDataset

3-minute pitch of your dataset to the class

    My 3 minute pitch can be found here: https://github.com/ysaismartinez/FinalDataSetProject/tree/FinalDataSetBranch/Video%20Presentation%20Pitch
    