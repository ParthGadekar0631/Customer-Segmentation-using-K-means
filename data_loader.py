import pandas as pd

def load_data(file_path):
    """Loads customer data from a CSV file."""
    try:
        data = pd.read_csv(file_path)
        print("Data Loaded Successfully!")
        return data
    except Exception as e:
        print(f"Error loading data: {e}")
        return None