import pandas as pd

# Load the data
df = pd.read_csv("sample_data.csv")

print("Original Data:")
print(df)

# Clean the data
df = df.dropna()
df = df.drop_duplicates()

# Save cleaned data
df.to_csv("cleaned_data.csv", index=False)

print("\nCleaned Data:")
print(df)