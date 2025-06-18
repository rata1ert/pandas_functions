import pandas as pd

def filter_by_region(df, region):
    return df[df['Region'].isin(region)]