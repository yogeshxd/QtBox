
# 🧾 Data Format Specification

QTBox expects tab-delimited M1 CSV files with the following format:

## Example

```

<DATE>        <TIME>       <OPEN>  <HIGH>  <LOW>   <CLOSE> <TICKVOL>
2024.01.02    00:01:00     2045.0  2045.5  2044.8  2045.2   110

```

## Required Columns

- `<DATE>` – format: YYYY.MM.DD
- `<TIME>` – format: HH:MM:SS
- `<OPEN>` – opening price
- `<HIGH>` – highest price
- `<LOW>` – lowest price
- `<CLOSE>` – closing price
- `<TICKVOL>` – tick volume

## Directory Example

```

history/
└── XAUUSD/
   └── M1.csv

```
