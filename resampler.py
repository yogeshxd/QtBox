import os
import pandas as pd
from datetime import timedelta


class DataLoader:
    def __init__(self, symbol):
        self.symbol = symbol
        self.base_df = None
        self.resampled_dfs = {}

    def load_data(self, start=None, end=None):
        file_path = f"history/{self.symbol}/M1.csv"
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"M1.csv file not found at: {file_path}")

        df = pd.read_csv(file_path, delimiter='\t')
        if '<DATE>' not in df.columns or '<TIME>' not in df.columns:
            raise ValueError("CSV must contain '<DATE>' and '<TIME>' columns.")

        df['time'] = pd.to_datetime(df['<DATE>'] + ' ' + df['<TIME>'], format="%Y.%m.%d %H:%M:%S")
        df = df.rename(columns={
            '<OPEN>': 'open',
            '<HIGH>': 'high',
            '<LOW>': 'low',
            '<CLOSE>': 'close',
            '<TICKVOL>': 'tick_volume'
        })
        df = df[['time', 'open', 'high', 'low', 'close', 'tick_volume']]
        if start:
            df = df[df['time'] >= pd.to_datetime(start)]
        if end:
            df = df[df['time'] <= pd.to_datetime(end)]
        df = df.sort_values('time').reset_index(drop=True)
        self.base_df = df
        self.resample_all_timeframes()

    def resample_all_timeframes(self):
        tf_map = {
            "M1": None,
            "M5": 5,
            "M15": 15,
            "H1": 60,
            "H4": 240
        }
        for tf, minutes in tf_map.items():
            if minutes is None:
                self.resampled_dfs[tf] = self.base_df
            else:
                self.resampled_dfs[tf] = self.resample_ohlc(self.base_df, minutes)

    def resample_ohlc(self, df, interval_minutes):
        df = df.copy().set_index('time')
        df['bucket'] = df.index.map(lambda ts: ts - timedelta(
            minutes=ts.minute % interval_minutes,
            seconds=ts.second,
            microseconds=ts.microsecond
        ))
        grouped = df.groupby('bucket').agg({
            'open': 'first',
            'high': 'max',
            'low': 'min',
            'close': 'last',
            'tick_volume': 'sum'
        }).reset_index().rename(columns={'bucket': 'time'})
        return grouped

    def fetch_rates(self, timeframe, start=None, end=None):
        if timeframe not in self.resampled_dfs:
            raise ValueError(f"Timeframe '{timeframe}' is not supported. Run load_csv_data() first.")
        df = self.resampled_dfs[timeframe]
        if df is None:
            raise ValueError(f"Data for timeframe '{timeframe}' is not available.")
        if start:
            df = df[df['time'] >= pd.to_datetime(start).tz_localize(None)]
        if end:
            df = df[df['time'] <= pd.to_datetime(end).tz_localize(None)]
        return df.copy()
