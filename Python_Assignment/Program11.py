import pandas as pd

def clean_csv_data(file_path):
    
    data = pd.read_csv(file_path)
    
    print("Original Data:")
    print(data)
    
    # Remove duplicate rows
    data.drop_duplicates(inplace=True)
    
    # Handle missing values (e.g., fill with the mean of the column)
    data.fillna(data.mean(), inplace=True)
    
    print("\nCleaned Data:")
    print(data)
    
    return data

# Example usage
file_path = 'example.csv'  
cleaned_data = clean_csv_data(file_path)
