import pathlib
import os
import json

import requests

# Download the JSON data from the CDC API
url = "https://data.cdc.gov/api/views/yni7-er2q/rows.json?accessType=DOWNLOAD"
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    data = response.json()
    print("Data successfully loaded.")

    # Print the entire structure of the data to see what it looks like
    print("Complete data structure:")
    print(data)  # Print the whole data to inspect its structure
else:
    print(f"Failed to download data. Status code: {response.status_code}")
