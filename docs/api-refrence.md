# 🧠 QTBox API Reference

## Class: `DataLoader`

### `__init__(symbol)`
- Initialize for a given symbol (e.g. `"XAUUSD"`).

---

### `load_data(start=None, end=None)`
- Loads M1 CSV and parses it.
- Filters by date if `start` or `end` are provided.
- Auto-resamples into M5, M15, H1, H4.

---

### `resample_all_timeframes()`
- Creates resampled versions of the base M1 data.

---

### `resample_ohlc(df, interval_minutes)`
- Internal method to resample using custom minute interval.

---

### `fetch_rates(timeframe, start=None, end=None)`
- Returns OHLCV DataFrame for a given timeframe (`M1`, `M5`, etc.).
