# datafun-03-analytics
# gitclone
# virtual environment 
    source .venv/bin/activate
# install dependencies
    source .venv/bin/activate
    python3 -m pip install --upgrade pip setuptools wheel
    python3 -m pip install -r requirements.txt
# Add demo-script.py and utils_logger.py
    source .venv/bin/activate
    python3 demo-script.py
# Run
# git add commit push
    git add .
    git commit -m "Add .gitignore and requirements.txt files"
    git push -u origin main
    git push
# Used data.gov to find the csv file: Electric Vehicle Population Data which shows the Battery Electric Vehicles (BEVs) and Plug-in Hybrid Electric Vehicles (PHEVs) that are currently registered through Washington State Department of Licensing (DOL).
# git add commit push
# Used data.gov to find the excel file: Annual Electricity Price by State which shows the annual data on the average price of retail electricity to consumers.
# git add commit push
# Used data.gov to find the JSON file: Mental Health Care in the Last 4 Weeks which shows the answers to a survey that gauged the impact of the pandemic on employment status, consumer spending, food security, housing, education disruptions, and dimensions of physical and mental wellness.
# git add commit push
# Used Project Gutenberg to find the txt file of William Wordsworth's poems. 
# git add commit push

# Had to try multiple ways of getting my files. It kept saying it couldn't find my csv file so I had to download a new csv file and put my csv file into my datafun-03-analytics folder and then open in vs code.

# Tried to get 5 different excel files to download into vs code. Some worked but most didn't. It keeps saying, "The file is not displayed in the text editor because it is either binary or uses an unsupported text encoding." I then tried to do the example and I was able to get it into vs code however, I could not perform any functions as it gave me the message above. 

# for the CSV file, I ordered the data by rating. 
    from pathlib import Path
import pandas as pd

# from utils_logger import logger
# Import from local project modules
from utils_logger import logger

# Declare Global Variables
fetched_folder_name: str = "example_data"
processed_folder_name: str = "foster_processed"

def organize_by_rating(file_path, rating_column='rating'):
    try:
        # Load the dataset into a pandas DataFrame
        df = pd.read_csv(file_path)
        
        # Clean up column names to remove any leading/trailing spaces
        df.columns = df.columns.str.strip()

        # Check if the rating column exists
        if rating_column not in df.columns:
            raise ValueError(f"The column '{rating_column}' does not exist in the dataset.")
        
        # Sort the data by the rating column (ascending or descending)
        sorted_df = df.sort_values(by=rating_column, ascending=False)  # Change to True for ascending order
        
        # Optionally, group the data by rating to see the number of entries per rating (if needed)
        grouped_by_rating = df.groupby(rating_column).size().reset_index(name='Count')
        
        # Return both sorted data and grouped data
        return sorted_df, grouped_by_rating

    except Exception as e:
        # If you have a logger, you can use logger.error() instead of print
        # logger.error(f"Error processing the file: {e}")
        print(f"Error processing the file: {e}")
        return None, None


def save_data_to_txt(sorted_data, grouped_data, output_file_path):
    try:
        # Ensure the processed folder exists
        output_file_path.parent.mkdir(parents=True, exist_ok=True)
        
        # Open the output file in write mode
        with output_file_path.open('w') as file:
            # Write Sorted Data
            file.write("Sorted Data by Rating:\n")
            file.write(sorted_data.to_string(index=False))
            file.write("\n\n")
            
            # Write Grouped Data
            file.write("Grouped Data by Rating:\n")
            file.write(grouped_data.to_string(index=False))
        
        print(f"Data successfully saved to {output_file_path}")
    except Exception as e:
        print(f"Error saving the data: {e}")

# Example usage
def main():
    # Specify the path to the CSV file (adjust based on your file location)
    file_path = Path(fetched_folder_name) / "netflix_titles.csv"  # Replace with the correct file path

    # Call the function to organize data by rating
    sorted_data, grouped_data = organize_by_rating(file_path)

    # Check if data was successfully processed
    if sorted_data is not None:
        print("Sorted Data by Rating:")
        print(sorted_data.head())  # Print first few rows of sorted data
        
        print("\nGrouped Data by Rating:")
        print(grouped_data)
        
        # Define the output file path for saving as .txt
        output_file_path = Path(processed_folder_name) / "netflix_data_by_rating.txt"

        # Call function to save the data as .txt file
        save_data_to_txt(sorted_data, grouped_data, output_file_path)

if __name__ == "__main__":
    main()

# For the Excel files I tried to find the average age, average spending, top 5 frequent car makes, group by a specific answer, and group by a certain age. I could not get anything to work for the excel files I tried. It was tough to find a URL to use for some reason. 
# The sorted_names.txt is the best I could get. 
# Then for the JSON file I wanted to count the occurences of different age groups
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
