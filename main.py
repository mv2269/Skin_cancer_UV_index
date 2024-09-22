import requests
import pandas as pd
from bs4 import BeautifulSoup
from dotenv import load_dotenv
import os
import time




# Coordinates for each state
state_coordinates = {
    'Alabama': (32.806671, -86.791130),
    'Alaska': (61.370716, -152.404419),
    'Arizona': (33.729759, -111.431221),
    'Arkansas': (34.969704, -92.373123),
    'California': (36.116203, -119.681564),
    'Colorado': (39.059811, -105.311104),
    'Connecticut': (41.597782, -72.755371),
    'Delaware': (39.318523, -75.507141),
    'Florida': (27.766279, -81.686785),
    'Georgia': (33.040619, -83.643074),
    'Hawaii': (21.094318, -157.498337),
    'Idaho': (44.240459, -114.478828),
    'Illinois': (40.349457, -88.986137),
    'Indiana': (39.849426, -86.258278),
    'Iowa': (42.011539, -93.210526),
    'Kansas': (39.063946, -98.383522),
    'Kentucky': (37.668140, -84.670067),
    'Louisiana': (31.169546, -91.867805),
    'Maine': (44.693947, -69.381927),
    'Maryland': (39.063946, -76.802101),
    'Massachusetts': (42.230171, -71.530106),
    'Michigan': (43.326618, -84.536095),
    'Minnesota': (45.694454, -93.900192),
    'Mississippi': (32.741646, -89.678696),
    'Missouri': (38.456085, -92.288368),
    'Montana': (46.921925, -110.454353),
    'Nebraska': (41.492537, -99.901810),
    'Nevada': (38.313515, -117.055374),
    'New Hampshire': (43.193852, -71.572395),
    'New Jersey': (40.298904, -74.521011),
    'New Mexico': (34.840515, -106.248482),
    'New York': (42.165726, -74.948051),
    'North Carolina': (35.630066, -79.806419),
    'North Dakota': (47.528912, -99.784012),
    'Ohio': (40.388783, -82.764915),
    'Oklahoma': (35.565342, -96.928917),
    'Oregon': (43.933305, -120.558201),
    'Pennsylvania': (40.590752, -77.209755),
    'Rhode Island': (41.680893, -71.511780),
    'South Carolina': (33.856892, -80.945007),
    'South Dakota': (44.299782, -99.438828),
    'Tennessee': (35.747845, -86.692345),
    'Texas': (31.054487, -97.563461),
    'Utah': (40.150032, -111.862434),
    'Vermont': (44.045876, -72.710686),
    'Virginia': (37.769337, -78.169968),
    'Washington': (47.400902, -121.490494),
    'West Virginia': (38.491226, -80.954613),
    'Wisconsin': (43.784440, -88.787868),
    'Wyoming': (42.755966, -107.302490)
}

# Visual Crossing API key
load_dotenv()
api_key = os.getenv('UV_API_KEY')


# Create a DataFrame to store the UV index
uv_data = []

for state, (lat, lon) in state_coordinates.items():
    # Use the correct date range for historical data (entire year 2022)
    time.sleep(2)  # Wait for 2 seconds before the next request

    url = f"https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{state},US/2022-01-01/2022-12-31?key={api_key}&include=uvindex"
    
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        if 'days' in data:
            uv_index = sum(day['uvindex'] for day in data['days']) / len(data['days'])  # Average UV index for 2022
            uv_data.append({'State': state, 'UV Index': uv_index})
        else:
            uv_data.append({'State': state, 'UV Index': None})
    else:
        print(f"Failed to retrieve UV data for {state}: {response.status_code}")
        uv_data.append({'State': state, 'UV Index': None})

# Convert the UV data into a DataFrame
uv_df = pd.DataFrame(uv_data)


# URL of the page
url = "https://quotewizard.com/news/skin-cancer-rates-by-state"

# Set headers to mimic a browser request
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"
}

# Send a GET request to the website
response = requests.get(url, headers=headers)

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find the table containing skin cancer rates
    table = soup.find('table')

    # Initialize lists to hold the data
    states = []
    rates = []

    # Iterate through table rows to extract data
    for row in table.find_all('tr')[1:]:  # Skip the header row
        columns = row.find_all('td')
        if len(columns) > 1:  # Ensure there are enough columns
            states.append(columns[0].get_text(strip=True))
            rates.append(columns[1].get_text(strip=True))

    # Create a DataFrame
    skin_cancer_df = pd.DataFrame({
        'State': states,
        'Skin Cancer Rate (per 100,000)': rates
    })

    
   
else:
    print("Failed to retrieve data:", response.status_code)

merged_df = pd.merge(skin_cancer_df, uv_df, on='State')
print(merged_df)
# Check correlation between UV Index and Skin Cancer Rates
correlation = merged_df['UV Index'].corr(merged_df['Skin Cancer Rate (per 100,000)'])
print(f"Correlation between UV Index and Skin Cancer Rate: {correlation}")
