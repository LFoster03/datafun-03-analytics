"""
This example file fetches a CSV file from the web 
and saves it to a local file named 2020_happiness.csv in a folder named example_data.

Please save a copy of the provided utils_logger.py file 
in the same folder as this file.
"""

#####################################
# Import Modules at the Top
#####################################

# Import from Python Standard Library
import pathlib

# Import from external packages
import requests

# Import from local project modules
from utils_logger import logger

#####################################
# Declare Global Variables
#####################################

fetched_folder_name = "example_data"

#####################################
# Define Functions
#####################################

def fetch_csv_file(folder_name: str, filename: str, url: str) -> None:
    """
    Fetch CSV data from the given URL and write it to a file.

    Args:
        folder_name (str): Name of the folder to save the file.
        filename (str): Name of the output file.
        url (str): URL of the CSV file to fetch.

    Returns:
        None

    Example:
        fetch_csv_file("data", "data.csv", "https://example.com/data.csv")
    """
    if not url:
        logger.error("The URL provided is empty. Please provide a valid URL.")
        return

    try:
        logger.info(f"Fetching CSV data from {url}...")
        response = requests.get(url)
        response.raise_for_status()
        write_csv_file(folder_name, filename, response.text)
        logger.info(f"SUCCESS: CSV file fetched and saved as {filename}")
    except requests.exceptions.HTTPError as http_err:
        logger.error(f"HTTP error occurred: {http_err}")
    except requests.exceptions.RequestException as req_err:
        logger.error(f"Request error occurred: {req_err}")

def write_csv_file(folder_name: str, filename: str, string_data: str) -> None:
    """
    Write CSV data to a file.

    Args:
        folder_name (str): Name of the folder to save the file.
        filename (str): Name of the output file.
        string_data (str): CSV content as a string.

    Returns:
        None
    """
    file_path = pathlib.Path(folder_name).joinpath(filename)
    try:
        logger.info(f"Writing CSV data to {file_path}...")
        file_path.parent.mkdir(parents=True, exist_ok=True)
        with file_path.open('w') as file:
            file.write(string_data)
        logger.info(f"SUCCESS: CSV data written to {file_path}")
    except IOError as io_err:
        logger.error(f"Error writing CSV data to {file_path}: {io_err}")

#####################################
# Define main() function
#####################################

def main():
    """
    Main function to demonstrate fetching CSV data.
    """
    csv_url = 'https://raw.githubusercontent.com/MainakRepositor/Datasets/master/World%20Happiness%20Data/2020.csv'
    logger.info("Starting CSV fetch demonstration...")
    fetch_csv_file(fetched_folder_name, "2020_happiness.csv", csv_url)

#####################################
# Conditional Execution
#####################################

if __name__ == '__main__':
    main()

# TODO: Run this script to ensure all functions work as intended.



"""
This example file fetches an Excel file from the web 
and saves it to a local file named feedback.xlsx in a folder named example_data.

Please save a copy of the provided utils_logger.py file 
in the same folder as this file.
"""

#####################################
# Import Modules at the Top
#####################################

# Import from Python Standard Library
import pathlib

# Import from external packages
import requests

# Import from local project modules
from utils_logger import logger

#####################################
# Declare Global Variables
#####################################

fetched_folder_name = "example_data"

#####################################
# Define Functions
#####################################

def fetch_excel_file(folder_name: str, filename: str, url: str) -> None:
    """
    Fetch Excel data from the given URL and write it to a file.

    Args:
        folder_name (str): Name of the folder to save the file.
        filename (str): Name of the output file.
        url (str): URL of the Excel file to fetch.

    Returns:
        None

    Example:
        fetch_excel_file("data", "data.xlsx", "https://example.com/data.xlsx")
    """
    if not url:
        logger.error("The URL provided is empty. Please provide a valid URL.")
        return

    try:
        logger.info(f"Fetching Excel data from {url}...")
        response = requests.get(url)
        response.raise_for_status()
        write_excel_file(folder_name, filename, response.content)
        logger.info(f"SUCCESS: Excel file fetched and saved as {filename}")
    except requests.exceptions.HTTPError as http_err:
        logger.error(f"HTTP error occurred: {http_err}")
    except requests.exceptions.RequestException as req_err:
        logger.error(f"Request error occurred: {req_err}")

def write_excel_file(folder_name: str, filename: str, binary_data: bytes) -> None:
    """
    Write Excel binary data to a file.

    Args:
        folder_name (str): Name of the folder to save the file.
        filename (str): Name of the output file.
        binary_data (bytes): Binary content of the Excel file.

    Returns:
        None
    """
    file_path = pathlib.Path(folder_name).joinpath(filename)
    try:
        logger.info(f"Writing Excel data to {file_path}...")
        file_path.parent.mkdir(parents=True, exist_ok=True)
        with file_path.open('wb') as file:
            file.write(binary_data)
        logger.info(f"SUCCESS: Excel data written to {file_path}")
    except IOError as io_err:
        logger.error(f"Error writing Excel data to {file_path}: {io_err}")

#####################################
# Define main() function
#####################################

def main():
    """
    Main function to demonstrate fetching Excel data.
    """
    excel_url = 'https://raw.githubusercontent.com/denisecase/datafun-03-analytics/main/hosted/Feedback.xlsx'
    logger.info("Starting Excel fetch demonstration...")
    fetch_excel_file(fetched_folder_name, "feedback.xlsx", excel_url)

#####################################
# Conditional Execution
#####################################

if __name__ == '__main__':
    main()

# TODO: Run this script to ensure all functions work as intended.


"""
This example file fetches JSON data of astronauts currently in space 
from the web and saves it to a local file named example_data/astronauts.json.

TODO: Save a copy of the provided utils_logger.py file 
in the same folder as this file.
"""

#####################################
# Import Modules at the Top
#####################################

# Import from Python Standard Library
import json
import pathlib

# Import from external packages
import requests

# Import from local project modules
from utils_logger import logger

#####################################
# Declare Global Variables
#####################################

fetched_folder_name = "example_data"

#####################################
# Define Functions
#####################################

def fetch_json_file(folder_name: str, filename: str, url: str) -> None:
    """
    Fetch JSON data from the given URL and write it to a file.

    Args:
        folder_name (str): Name of the folder to save the file.
        filename (str): Name of the output file.
        url (str): URL of the JSON file to fetch.

    Returns:
        None

    Example:
        fetch_json_file("data", "data.json", "https://example.com/data.json")
    """
    if not url:
        logger.error("The URL provided is empty. Please provide a valid URL.")
        return

    try:
        logger.info(f"Fetching JSON data from {url}...")
        response = requests.get(url)
        response.raise_for_status()
        write_json_file(folder_name, filename, response.json())
        logger.info(f"SUCCESS: JSON file fetched and saved as {filename}")
    except requests.exceptions.HTTPError as http_err:
        logger.error(f"HTTP error occurred: {http_err}")
    except requests.exceptions.RequestException as req_err:
        logger.error(f"Request error occurred: {req_err}")

def write_json_file(folder_name: str, filename: str, json_data: dict) -> None:
    """
    Write JSON data to a file.

    Args:
        folder_name (str): Name of the folder to save the file.
        filename (str): Name of the output file.
        json_data (dict): JSON data to write to the file.

    Returns:
        None
    """
    file_path = pathlib.Path(folder_name).joinpath(filename)
    try:
        logger.info(f"Writing JSON data to {file_path}...")
        file_path.parent.mkdir(parents=True, exist_ok=True)
        with file_path.open('w') as file:
            json.dump(json_data, file, indent=4)
        logger.info(f"SUCCESS: JSON data written to {file_path}")
    except IOError as io_err:
        logger.error(f"Error writing JSON data to {file_path}: {io_err}")

#####################################
# Define main() function
#####################################

def main():
    """
    Main function to demonstrate fetching JSON data.
    """
    json_url = 'http://api.open-notify.org/astros.json'
    logger.info("Starting JSON fetch demonstration...")
    fetch_json_file(fetched_folder_name, "astros.json", json_url)

#####################################
# Conditional Execution
#####################################

if __name__ == '__main__':
    main()

# TODO: Run this script to ensure all functions work as intended.


"""
This example file fetches a text file of Romeo and Juliet from the web 
and saves it to a local file named romeo.txt in a folder named example_data.

Please save a copy of the provided utils_logger.py file 
in the same folder as this file.
"""

#####################################
# Import Modules at the Top
#####################################

# Import from Python Standard Library
import pathlib

# Import from external packages
import requests

# Import from local project modules
from utils_logger import logger

#####################################
# Declare Global Variables
#####################################

fetched_folder_name = "example_data"

#####################################
# Define Functions
#####################################

def fetch_txt_file(folder_name: str, filename: str, url: str) -> None:
    """
    Fetch text data from the given URL and write it to a file.

    Args:
        folder_name (str): Name of the folder to save the file.
        filename (str): Name of the output file.
        url (str): URL of the text file to fetch.

    Returns:
        None

    Example:
        fetch_txt_file("data", "romeo.txt", "https://example.com/romeo.txt")
    """
    if not url:
        logger.error("The URL provided is empty. Please provide a valid URL.")
        return

    try:
        logger.info(f"Fetching text data from {url}...")
        response = requests.get(url)
        response.raise_for_status()
        write_txt_file(folder_name, filename, response.text)
        logger.info(f"SUCCESS: Text file fetched and saved as {filename}")
    except requests.exceptions.HTTPError as http_err:
        logger.error(f"HTTP error occurred: {http_err}")
    except requests.exceptions.RequestException as req_err:
        logger.error(f"Request error occurred: {req_err}")

def write_txt_file(folder_name: str, filename: str, string_data: str) -> None:
    """
    Write text data to a file.

    Args:
        folder_name (str): Name of the folder to save the file.
        filename (str): Name of the output file.
        string_data (str): Text content to write to the file.

    Returns:
        None
    """
    file_path = pathlib.Path(folder_name).joinpath(filename)
    try:
        logger.info(f"Writing data to {file_path}...")
        file_path.parent.mkdir(parents=True, exist_ok=True)
        with file_path.open('w') as file:
            file.write(string_data)
        logger.info(f"SUCCESS: Data written to {file_path}")
    except IOError as io_err:
        logger.error(f"Error writing to file {file_path}: {io_err}")

#####################################
# Define main() function
#####################################

def main():
    """
    Main function to demonstrate fetching text data.
    """
    txt_url = 'https://raw.githubusercontent.com/denisecase/datafun-03-analytics/main/hosted/romeo.txt'
    logger.info("Starting text fetch demonstration...")
    fetch_txt_file(fetched_folder_name, "romeo.txt", txt_url)

#####################################
# Conditional Execution
#####################################

if __name__ == '__main__':
    main()

# TODO: Run this as a script to test that all functions work as intended.