# scripts/clean_prepare.py

import pandas as pd

df = pd.read_csv("data/raw_data.csv")

# Remove duplicates
df.drop_duplicates(subset=["Title", "Brand"], inplace=True)

# Clean prices, reviews, ratings
df["Selling Price"] = df["Selling Price"].str.replace("₹", "").str.replace(",", "").astype(float)
df["Reviews"] = pd.to_numeric(df["Reviews"], errors='coerce').fillna(0).astype(int)
df["Rating"] = pd.to_numeric(df["Rating"], errors='coerce').fillna(0)

# Fill brand if empty
df["Brand"] = df["Brand"].replace("Unknown", pd.NA).fillna(df["Title"].str.split().str[0])

# Save cleaned data
df.to_csv("data/cleaned_data.csv", index=False)
