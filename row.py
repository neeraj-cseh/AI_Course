import pandas as pd
from requests import head

# df = pd.read_csv("sales_data_sample.csv", encoding = "latin1")
# df = pd.read_excel("SampleSuperstore.xlsx")
df = pd.read_json("sample_Data.json")
print("Top 4 rows of the DataFrame:")
print(df.head(4))

print("\nBottom 4 rows of the DataFrame:")
print(df.tail(4))