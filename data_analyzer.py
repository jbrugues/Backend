import yfinance as yf
import pandas as pd
from claude_helper import ask_claude

# Download some stock data
ticker = "AAPL"
data = yf.download(ticker, start="2024-01-01", end="2024-12-31", progress=False)

# If columns are multi-indexed, flatten them
if isinstance(data.columns, pd.MultiIndex):
    data.columns = data.columns.get_level_values(0)

# Calculate some basic statistics and convert to float
stats = {
    "mean_close": float(data['Close'].mean()),
    "std_close": float(data['Close'].std()),
    "max_close": float(data['Close'].max()),
    "min_close": float(data['Close'].min()),
    "total_days": len(data)
}

# Create a prompt for Claude with the data
prompt = f"""
I have stock data for {ticker} from 2024. Here are some statistics:
- Average closing price: ${stats['mean_close']:.2f}
- Standard deviation: ${stats['std_close']:.2f}
- Highest close: ${stats['max_close']:.2f}
- Lowest close: ${stats['min_close']:.2f}
- Trading days: {stats['total_days']}

Based on these statistics, what can you tell me about this stock's volatility in 2024? Keep it brief.
"""

# Ask Claude to analyze
analysis = ask_claude(prompt)

print(f"\n{'='*60}")
print(f"Claude's Analysis of {ticker}")
print(f"{'='*60}\n")
print(analysis)