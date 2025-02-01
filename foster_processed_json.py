import json
import requests

# Function to download and process the CDC data
def process_cdc_data(url):
    # Download the JSON data from the provided URL
    response = requests.get(url)
    
    # Check if the request was successful (HTTP Status Code 200)
    if response.status_code == 200:
        data = response.json()  # Parse the JSON data into a Python object
    else:
        print(f"Failed to retrieve data. HTTP Status code: {response.status_code}")
        return None
    
    # Extract the rows from the dataset (usually in 'data' or 'rows' field, depending on structure)
    rows = data.get('data', [])
    
    # Example of analyzing the data: Let's say we're interested in counting the occurrences of a specific column
    # (e.g. assume there's a column 'age_group' and we want to count how many people fall into each group)
    
    # Count occurrences of a specific field (e.g., 'age_group')
    age_group_counts = {}
    for row in rows:
        age_group = row[1]  # Assuming the 'age_group' is in the second column (adjust according to actual data)
        if age_group in age_group_counts:
            age_group_counts[age_group] += 1
        else:
            age_group_counts[age_group] = 1
    
    # Print or return the analysis results
    print("Age Group Counts:", age_group_counts)
    
    # Save the analysis result to a .txt file
    with open('cdc_data_analysis.txt', 'w') as file:
        file.write("Age Group Counts:\n")
        for age_group, count in age_group_counts.items():
            file.write(f"{age_group}: {count}\n")
    
    print("Data analysis saved to cdc_data_analysis.txt")

# URL for the CDC data
url = "https://data.cdc.gov/api/views/yni7-er2q/rows.json?accessType=DOWNLOAD"

# Run the function to process and analyze the data
process_cdc_data(url)
