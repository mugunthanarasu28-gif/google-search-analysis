import os  # Standard library to handle folders
from src.data_cleaning import clean_data
from src.analysis import get_top_queries
from src.visualization import plot_clicks_over_time

def run_pipeline():
    print("Starting Analysis...")

    # ... (keep your existing folder check and cleaning code)
    data = clean_data('data/sample_data.csv')
    
    if data is not None:
        # Save CSV
        top_results = get_top_queries(data)
        top_results.to_csv('outputs/results.csv', index=False)
        
        # Save Plot
        plot_clicks_over_time(data) # Add this
        print("Success! Check your outputs folder.")
    
    # 1. Create the outputs folder if it doesn't exist
    if not os.path.exists('outputs'):
        os.makedirs('outputs')
        print("Created 'outputs' directory.")

    # 2. Run your logic
    data = clean_data('data/sample_data.csv')
    
    if data is not None:
        top_results = get_top_queries(data)
        
        # 3. Save results
        top_results.to_csv('outputs/results.csv', index=False)
        print("Success! Check outputs/results.csv")
    else:
        print("Analysis failed due to data issues.")

if __name__ == "__main__":
    run_pipeline()