import pandas as pd

def descending_sort(df):
    return df.sort_values(by = 'Total sales', ascending = False)