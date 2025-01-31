from pathlib import Path
import pandas as pd

# Optional: Uncomment if you're using a logger
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

