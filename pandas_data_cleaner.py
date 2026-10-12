import pandas as pd
import numpy as np

def clean_messy_dataset(file_path):
    """Cleans a messy business dataset: handles nulls, duplicates, and formatting."""
    # Load data (assuming a generic CSV)
    df = pd.read_csv(file_path)
    
    # 1. Remove exact duplicate rows
    df.drop_duplicates(inplace=True)
    
    # 2. Standardize column names (lowercase, replace spaces with underscores)
    df.columns = df.columns.str.lower().str.replace(' ', '_')
    
    # 3. Fill missing numerical values with the median
    num_cols = df.select_dtypes(include=[np.number]).columns
    df[num_cols] = df[num_cols].fillna(df[num_cols].median())
    
    # 4. Standardize text columns (strip whitespace, title case)
    str_cols = df.select_dtypes(include=['object']).columns
    for col in str_cols:
        df[col] = df[col].astype(str).str.strip().str.title()
        
    # Save cleaned data
    clean_path = file_path.replace('.csv', '_cleaned.csv')
    df.to_csv(clean_path, index=False)
    print(f"Data cleaned and saved to {clean_path}")
    return df
