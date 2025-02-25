import pandas as pd
import os

def main():
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
    # Define the order of months 
    month_order = ["jan", "feb", "mar", "apr", "may", "jun", "jul", "aug", "sep", "oct", "nov", "dec"]

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

    directory = os.path.join(os.path.dirname(os.getcwd()), 'data/processed')
    
    # Ensure the directory exists
    os.makedirs(directory, exist_ok=True)

    file_path = os.path.join(directory, 'prep_bank_marketing.csv')
    bank_prep.to_csv(file_path, index=False)
    print(f"Preprocessed Dataset saved to '{file_path}'")

if __name__ == '__main__':
    main()
