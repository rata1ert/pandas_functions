import pandas as pd

def add_total_sales(df):
    df['Total sales'] = df['Units Sold'] * df['Unit Price']
    return df