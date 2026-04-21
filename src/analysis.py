def get_top_queries(df, top_n=10):
    # Sort by clicks to see what's driving traffic
    return df.sort_values(by='Clicks', ascending=False).head(top_n)