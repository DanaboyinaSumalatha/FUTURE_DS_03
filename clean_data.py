import pandas as pd

# Load only first 200000 rows
df = pd.read_csv("2019-Nov.csv", nrows=200000)

# Show first 5 rows
print(df.head())

# Dataset information
print(df.info())

# Check missing values
print(df.isnull().sum())

# Remove duplicate rows
df = df.drop_duplicates()

# Remove rows with missing sessions
df = df.dropna(subset=["user_session"])

# Create Funnel Stage Column
df["funnel_stage"] = df["event_type"].map({
    "view": "Product View",
    "cart": "Add to Cart",
    "purchase": "Purchase"
})

# Keep only useful funnel events
df = df[df["event_type"].isin(["view", "cart", "purchase"])]

# Save cleaned dataset
df.to_csv("cleaned_funnel_data.csv", index=False)

print("Data cleaned successfully!")