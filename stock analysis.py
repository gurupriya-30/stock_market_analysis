import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# -----------------------------------
# 1. Load Dataset
# -----------------------------------

df = pd.read_csv("stock_data.csv")

# Convert Date column
# df["Date"] = pd.to_datetime(df["Date"])
df["Date"] = pd.to_datetime(df["Date"], format="%d-%m-%Y")
print("\n========== STOCK MARKET DATA ==========\n")
print(df)

# -----------------------------------
# 2. Basic Information
# -----------------------------------

print("\n========== DATA INFORMATION ==========\n")
print(df.info())

print("\n========== STATISTICAL SUMMARY ==========\n")
print(df.describe())

# -----------------------------------
# 3. Moving Average
# -----------------------------------

df["MA5"] = df["Close"].rolling(5).mean()

# -----------------------------------
# 4. Daily Returns
# -----------------------------------

df["Daily_Return"] = df["Close"].pct_change() * 100
# print(df["Daily_Return"])

# -----------------------------------
# 5. Volatility
# -----------------------------------

df["Volatility"] = df["Daily_Return"].rolling(5).std()
# print(df["Volatility"] )
# -----------------------------------
# 6. Price Trend
# -----------------------------------

plt.figure(figsize=(10, 5))

plt.plot(
    df["Date"],
    df["Close"],
    marker="o",
    label="Closing Price"
)

plt.title("Stock Price Trend")
plt.xlabel("Date")
plt.ylabel("Price")
plt.xticks(rotation=45)
plt.legend()
plt.grid()

plt.tight_layout()
plt.show()

# -----------------------------------
# 7. Moving Average Chart
# -----------------------------------

plt.figure(figsize=(10, 5))

plt.plot(
    df["Date"],
    df["Close"],
    label="Closing Price"
)

plt.plot(
    df["Date"],
    df["MA5"],
    label="5-Day Moving Average"
)

plt.title("Stock Price and Moving Average")
plt.xlabel("Date")
plt.ylabel("Price")
plt.xticks(rotation=45)
plt.legend()
plt.grid()

plt.tight_layout()
plt.show()

# -----------------------------------
# 8. Daily Return Chart
# -----------------------------------

plt.figure(figsize=(10, 5))

plt.plot(
    df["Date"],
    df["Daily_Return"],
    marker="o"
)

plt.axhline(0, linestyle="--")

plt.title("Daily Stock Returns")
plt.xlabel("Date")
plt.ylabel("Return (%)")
plt.xticks(rotation=45)
plt.grid()

plt.tight_layout()
plt.show()

# -----------------------------------
# 9. Volatility Chart
# -----------------------------------

plt.figure(figsize=(10, 5))

plt.plot(
    df["Date"],
    df["Volatility"],
    marker="o"
)

plt.title("Stock Volatility")
plt.xlabel("Date")
plt.ylabel("Volatility")
plt.xticks(rotation=45)
plt.grid()

plt.tight_layout()
plt.show()

# -----------------------------------
# 10. Trading Volume
# -----------------------------------

plt.figure(figsize=(10, 5))

plt.bar(
    df["Date"],
    df["Volume"]
)

plt.title("Trading Volume")
plt.xlabel("Date")
plt.ylabel("Volume")
plt.xticks(rotation=45)

plt.tight_layout()
plt.show()

# -----------------------------------
# 11. Correlation Heatmap
# -----------------------------------

plt.figure(figsize=(8, 6))

correlation = df[
    ["Open", "High", "Low", "Close", "Volume"]
].corr()

sns.heatmap(
    correlation,
    annot=True,
    cmap="coolwarm"

)

plt.title("Stock Data Correlation")

plt.tight_layout()
plt.show()

# -----------------------------------
# 12. Final Analysis
# -----------------------------------

latest_price = df["Close"].iloc[-1]
average_price = df["Close"].mean()
average_return = df["Daily_Return"].mean()

print("\n========== FINAL ANALYSIS ==========\n")

print("Latest Closing Price :", latest_price)
print("Average Closing Price:", round(average_price, 2))
print("Average Daily Return :", round(average_return, 2), "%")

if latest_price > average_price:
    print("Trend : Positive 📈")
else:
    print("Trend : Negative 📉")

if average_return > 0:
    print("Market Movement : Generally Positive")
else:
    print("Market Movement : Generally Negative")

print("\n========== PROJECT COMPLETED ==========")