import pandas as pd
import os

def main():
    """
    Preprocess the Bank Marketing dataset and saves it to a CSV file in the 'data/processed/' directory.

    The function read in the raw dataset, carry out mapping to the job column and assign year to the corresponding
    observation before saving it as a CSV file at the specified directory path 'data/processed/prep_bank_marketing.csv'.
    """
    bank_prep = pd.read_csv("../data/raw/bank_marketing.csv")

    # Preprocessing for job categories
    job_mapping = {
        "admin.": "Employed",
        "management": "Employed",
        "housemaid": "Employed",
        "entrepreneur": "Employed",
        "blue-collar": "Employed",
        "self-employed": "Employed",
        "technician": "Employed",
        "services": "Employed",
        "unemployed": "Unemployed",
        "unknown": "Unknown",
        "student": "Student",
        "retired": "Retired"
    }

    # Apply the mapping
    bank_prep["job_prep"] = bank_prep["job"].replace(job_mapping).fillna("Unknown")

    # Preprocessing for years

    # Initialize variables
    year = 2008 
    years = []
    prev_month = None  # Keep track of previous month

    # Assign years based on month order
    for month in bank_prep["month"]:
        if prev_month == "dec" and month == "jan":  # If transition from Dec -> Jan, increment year
            year += 1
        years.append(year)
        prev_month = month  # Update previous month

    # Assign computed years to DataFrame
    bank_prep["year"] = years

    # Convert 'y' column to numeric values
    bank_prep['y_numeric'] = bank_prep['y'].map({'yes': 1, 'no': 0})

    # Standardize job categories
    bank_prep['job_prep'] = bank_prep['job_prep'].str.lower().str.strip()

    # Remove unnecessary columns
    bank_prep.drop(columns=['job', 'default', 'housing', 'contact', 'day_of_week', 'month', 'pdays', 'poutcome'], inplace=True)

    directory = os.path.join(os.path.dirname(os.getcwd()), 'data/processed')
    
    # Ensure the directory exists
    os.makedirs(directory, exist_ok=True)

    file_path = os.path.join(directory, 'prep_bank_marketing.csv')
    bank_prep.to_csv(file_path, index=False)
    print(f"Preprocessed Dataset saved to '{file_path}'")

    file_path = os.path.join(directory, 'prep_bank_marketing.parquet')
    bank_prep.to_parquet(file_path, index=False)
    print(f"Preprocessed Dataset saved to '{file_path}'")

if __name__ == '__main__':
    main()
