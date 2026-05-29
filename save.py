import pandas as pd

data = {
    "Name": ["Mala", "Neeraj", "Srinivas"],
    "Age": [23, 24, 25],
    "City": ["Kurrnool", "Nandyla", "Hyderabad"]
}

df = pd.DataFrame(data)
print(df)
df.to_json("output.json", index=False)