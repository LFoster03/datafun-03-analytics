import pathlib
import statistics
import pandas as pd


def read_excel_data(file_path):
    try:
        # For .xlsx files, use openpyxl as the engine
        df = pd.read_excel(file_path, engine='openpyxl')  # Specify engine if needed
        print(df.head())  # Display the first few rows
        return df
    except Exception as e:
        print(f"Error reading the Excel file: {e}")

# Example usage
file_path = "avgprice_annual.xlsx"  # Replace with the actual path to your file
df = read_excel_data(file_path)

def read_excel_data(file_path):
    try:
        # Read the Excel file into a pandas DataFrame
        df = pd.read_excel(file_path)  # Make sure 'openpyxl' is installed if it's an xlsx file
        print(df.head())  # Display the first few rows
        return df
    except Exception as e:
        print(f"Error reading the Excel file: {e}")

# Example usage
file_path = "example_data/avgprice_annual.xlsx"  # Replace with the actual path to your file
df = read_excel_data(file_path)

def calculate_statistics(file_path, column_name):
    try:
        # Load the dataset into a pandas DataFrame
        df = pd.read_csv(file_path)

        # Clean up column names to remove any leading/trailing spaces
        df.columns = df.columns.str.strip()

        # Check if the column exists in the dataset
        if column_name not in df.columns:
            raise ValueError(f"The column '{column_name}' does not exist in the dataset.")
        
        # Calculate mean, median, and mode
        mean_value = df[column_name].mean()
        median_value = df[column_name].median()
        mode_value = df[column_name].mode()[0]  # mode() returns a series, so we take the first value

        # Return the results as a dictionary
        return {
            "mean": mean_value,
            "median": median_value,
            "mode": mode_value
        }

    except Exception as e:
        print(f"Error processing the file: {e}")
        return None


# Example usage
file_path = "example_data/avgprice_annual.xlsx"  # Replace with the actual path to your downloaded excel file
column_name = "Total"  # Replace with the actual column name that holds the price data

statistics = calculate_statistics(file_path, column_name)
if statistics:
    print(f"Mean: {statistics['mean']}")
    print(f"Median: {statistics['median']}")
    print(f"Mode: {statistics['mode']}")
