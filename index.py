python
import pandas as pd
import requests
import os

# Define the dataset URL
url = "https://www.abudhabi.opendata.ae/resources/DL02-Mobdiaa-Activities-ADRA-OD-006-AMO_0.xlsx"
output_file = "Mobdiaa_Activities_Dataset.xlsx"

# Downloading the dataset
def download_dataset(url, output_file):
    response = requests.get(url)
    if response.status_code == 200:
        with open(output_file, 'wb') as file:
            file.write(response.content)
        print(f"Dataset downloaded successfully and saved as {output_file}.")
    else:
        print("Failed to download dataset. Please check the URL.")

# Load the dataset into a DataFrame
def load_dataset(file_path):
    try:
        df = pd.read_excel(file_path)
        print("Dataset loaded successfully.")
        return df
    except Exception as e:
        print(f"Error loading dataset: {e}")
        return None

# Analyze the dataset
def analyze_dataset(df):
    if df is not None:
        print("Dataset Information:")
        print(df.info())
        print("\nFirst 5 rows:")
        print(df.head())

# Main script
if __name__ == "__main__":
    download_dataset(url, output_file)
    data = load_dataset(output_file)
    analyze_dataset(data)
