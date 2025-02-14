import pandas as pd
import os
from ucimlrepo import fetch_ucirepo 

def download_raw_dataset():
    """
    Downloads the Bank Marketing dataset from the UCI Machine Learning Repository.

    The function fetches the dataset using the ucimlrepo library, separates the features and target variables, 
    and returns a combined pandas DataFrame with both features and target variables.

    Returns:
        pd.DataFrame: A pandas DataFrame containing the full dataset with features and target variable.
    """
    # Fetch dataset
    bank_marketing = fetch_ucirepo(id=222)
    
    # Data (as pandas dataframes)
    X = bank_marketing.data.features
    y = bank_marketing.data.targets
    
    # Join the data to make a full dataset
    complete_data = pd.concat([X, y], axis=1)
    
    return complete_data


def export_raw_dataset():
    """
    Downloads the Bank Marketing dataset and saves it to a CSV file in the 'data/raw/' directory.

    The function fetches the dataset, combines features and target variables, and saves it as a CSV file
    at the specified directory path 'data/raw/bank_marketing.csv'.
    """
    # Download the dataset
    bank_data = download_raw_dataset()
    directory = os.path.join(os.path.dirname(os.getcwd()), 'data/raw')

    # Ensure the directory exists
    os.makedirs(directory, exist_ok=True)

    # Save to CSV
    file_path = os.path.join(directory, 'bank_marketing.csv')
    bank_data.to_csv(file_path, index=False)

    print(f"Dataset saved to '{file_path}'")

export_raw_dataset()