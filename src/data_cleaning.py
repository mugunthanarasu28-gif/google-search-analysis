import pandas as pd

def clean_data(file_path):
    df = pd.read_csv(file_path)
    
    # 1. Strip whitespace from column names (common culprit)
    df.columns = df.columns.str.strip()
    
    # 2. Check if 'Date' exists (case-sensitive)
    if 'Date' not in df.columns:
        print(f"Error: Could not find 'Date' column. Available columns are: {list(df.columns)}")
        # Optional: Try to find 'date' lowercase if 'Date' fails
        if 'date' in df.columns:
            df.rename(columns={'date': 'Date'}, inplace=True)
        else:
            return None

    df['Date'] = pd.to_datetime(df['Date'])
    df = df.fillna(0)
    return df