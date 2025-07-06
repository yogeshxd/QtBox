# 🧠 QTBox — Quant Toolkit Box

**QTBox** is your all-in-one **Swiss Army Knife for algorithmic trading** — a lightweight, modular toolkit built to handle market data like a pro. Whether you're backtesting strategies, resampling tick data, or building live trading signals, QTBox gives you a fast, flexible foundation to build on.

---

## 🚀 Features

- 📦 **Modular Architecture** – Easy to extend with new tools as your quant needs grow.
- ⏱️ **Smart Resampling** – Quickly convert M1 data to M5, M15, H1, or custom frames.
- 🔍 **Precise Time Filtering** – Load just the data you need with flexible time slicing.
- 📊 **Clean OHLCV Structure** – Standardizes and prepares your data for backtesting, modeling, or visualizing.
- ✅ **Plug & Play Ready** – Just drop in your M1 CSV and go.

---

## 🛠️ Installation

```bash
git clone https://github.com/yogeshxd/qtbox.git
cd qtbox
pip install -r requirements.txt
````

---

## 📈 Usage

```python
from qtbox.dataloader import DataLoader

# Initialize loader for a given symbol (e.g., XAUUSD)
dl = DataLoader("XAUUSD")

# Load M1 data and auto-resample into common timeframes
dl.load_data(start="2024-01-01", end="2024-12-31")

# Fetch M15 resampled OHLC data
m15_df = dl.fetch_rates("M15")

# Display preview
print(m15_df.head())
```

---

## 🧩 Coming Soon

> QTBox is evolving. Future versions will include:

* 📉 Built-in candlestick + volume plotting
* 🧠 Indicator engine (MA, RSI, MACD, etc.)
* ⚖️ Lot size & margin calculator for MT5
* 🔌 MT5 Live Connector
* 📤 Parquet/Feather export support
* ⏳ Gap detection & data quality checks
* 🧪 Pytest-powered test suite
* 🧱 CLI support: `qtbox --symbol EURUSD --plot H1`

---

## 🧪 Sample Data Format

QTBox expects `M1.csv` with the following structure (`TAB-delimited`):

```
<DATE>        <TIME>       <OPEN>  <HIGH>  <LOW>   <CLOSE> <TICKVOL>
2024.01.02    00:01:00     2045.0  2045.5  2044.8  2045.2   110
```

Just place it inside:

```
history/
 └── XAUUSD/
     └── M1.csv
```

---

## 👨‍💻 Contributing

Pull requests are welcome! Please open an issue first if you want to add a major feature. Let's build the ultimate quant toolkit together 💡

---

## 📜 License

MIT License — free to use, modify, and contribute.

---

## 📎 Stay Updated

Star ⭐ this repo and watch for updates — more modules coming soon!
