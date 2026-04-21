import matplotlib.pyplot as plt
import seaborn as sns
import os

def plot_clicks_over_time(df):
    plt.figure(figsize=(10, 6))
    
    # Sort by date for a proper line chart
    df = df.sort_values('Date')
    
    # Create the plot
    sns.lineplot(data=df, x='Date', y='Clicks', marker='o')
    plt.title('Google Search Clicks Over Time')
    plt.xticks(rotation=45)
    
    # Ensure plots directory exists
    if not os.path.exists('outputs/plots'):
        os.makedirs('outputs/plots')
        
    plt.tight_layout()
    plt.savefig('outputs/plots/clicks_trend.png')
    print("Chart saved to outputs/plots/clicks_trend.png")
    plt.show()
    