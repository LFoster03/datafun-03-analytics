# Import Modules
import pathlib
import requests
from utils_logger import logger  # Assumes utils_logger.py is in the same folder

# Declare the folder where you want to save the CSV file
fetched_folder_name = "example_data"

def fetch_csv_file(folder_name: str, filename: str, url: str) -> None:
    """
    Fetch CSV data from the given URL and write it to a file.
    
    Arguments:
        folder_name (str): Name of the folder to save the file.
        filename (str): Name of the output file.
        url (str): URL of the CSV file to fetch.
    """
    if not url:
        logger.error("The URL provided is empty. Please provide a valid URL.")
        return

    try:
        logger.info(f"Fetching CSV data from {url}...")
        response = requests.get(url)  # Make a GET request to the URL
        response.raise_for_status()  # Raise an error for bad responses (404, 500, etc.)
        
        # Write the CSV data to a local file
        write_csv_file(folder_name, filename, response.text)
        
        logger.info(f"SUCCESS: CSV file fetched and saved as {filename}")
    except requests.exceptions.HTTPError as http_err:
        logger.error(f"HTTP error occurred: {http_err}")  # Log HTTP errors
    except requests.exceptions.RequestException as req_err:
        logger.error(f"Request error occurred: {req_err}")  # Log other request errors

def write_csv_file(folder_name: str, filename: str, string_data: str) -> None:
    """
    Write the CSV data to a file in the specified folder.
    
    Arguments:
        folder_name (str): The folder where the file will be saved.
        filename (str): The name of the output file.
        string_data (str): CSV content as a string.
    """
    file_path = pathlib.Path(folder_name).joinpath(filename)  # Path to save the file
    
    try:
        logger.info(f"Writing CSV data to {file_path}...")
        file_path.parent.mkdir(parents=True, exist_ok=True)  # Create folder if it doesn't exist
        with file_path.open('w') as file:
            file.write(string_data)  # Write the CSV data to the file
        logger.info(f"SUCCESS: CSV data written to {file_path}")
    except IOError as io_err:
        logger.error(f"Error writing CSV data to {file_path}: {io_err}")  # Log file writing errors

def main():
    """
    Main function to demonstrate fetching CSV data.
    """
    # URL of the Electric Vehicle Population Data CSV file from Data.gov
    csv_url = 'https://www.kaggle.com/datasets/anandshaw2001/netflix-movies-and-tv-shows'
    
    logger.info("Starting CSV fetch demonstration...")
    
    # Call the function to fetch the CSV file and save it to the folder
    fetch_csv_file(fetched_folder_name, "netflix-titles.csv", csv_url)

if __name__ == '__main__':
    main()
