# 🚀 Getting Started with QTBox

Welcome to **QTBox** — a modular toolkit for quant traders.

## 1. Install Dependencies

```bash
pip install -r requirements.txt
````

## 2. Project Structure

```
QTBox/
 ├── qtbox/
 │    └── resampler.py
 ├── history/
 │    └── SYMBOL/
 │         └── M1.csv
 └── main.py
```

## 3. Load & Resample

```python
from qtbox.resampler import DataLoader

dl = DataLoader("XAUUSD")
dl.load_data(start="2024-01-01", end="2024-12-31")
h1_df = dl.fetch_rates("H1")
print(h1_df.tail())
```

> ⚠️ Ensure your `M1.csv` follows the [data format spec](./data-format.md).
