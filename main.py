import pandas as pd
from src.filter_by_region import filter_by_region

df = pd.read_excel("data/sales_example.xlsx")
region = [input("Введите регион: ")]
result = filter_by_region(df, region)
print (result)