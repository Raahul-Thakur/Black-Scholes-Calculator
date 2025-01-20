import yfinance as yf
import os

def fetch_historical_data(ticker="AAPL", start_date="2020-01-01", end_date="2023-01-01", output_path="src/data/historical_data.csv"):
    """
    Fetch historical stock data for the given ticker using yfinance and save it as a CSV file.

    Parameters:
    - ticker (str): Stock ticker symbol (e.g., "AAPL").
    - start_date (str): Start date in "YYYY-MM-DD" format.
    - end_date (str): End date in "YYYY-MM-DD" format.
    - output_path (str): Path to save the CSV file.

    Returns:
    - pandas.DataFrame: The fetched historical data.
    """
    print(f"Fetching historical data for {ticker} from {start_date} to {end_date}...")
    
    # Fetch data using yfinance
    data = yf.download(ticker, start=start_date, end=end_date)
    
    # Ensure the output directory exists
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    
    # Save the data to CSV
    data.to_csv(output_path)
    print(f"Data saved to {output_path}")
    
    return data

# Example usage
if __name__ == "__main__":
    fetch_historical_data(ticker="AAPL", start_date="2020-01-01", end_date="2023-01-01")
