import pandas as pd
from src.filter_by_region import filter_by_region
from src.add_total_sales import add_total_sales
from src.descending_sort import descending_sort
df = pd.read_excel("data/sales_example.xlsx")
region = [input("Введите регион: ")]
result = descending_sort(add_total_sales(filter_by_region(df, region))).head(10)
print (result)