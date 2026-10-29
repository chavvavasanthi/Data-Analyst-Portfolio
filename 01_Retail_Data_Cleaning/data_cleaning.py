
import pandas as pd

# Load raw customer data
df = pd.read_csv("customer_data_raw.csv")

print("Original rows:", len(df))
print("Original columns:", df.columns.tolist())

# Remove extra empty columns
df = df.loc[:, ~df.columns.str.startswith("Unnamed")]

# Remove completely empty rows
df = df.dropna(how="all")

# Remove rows without CustomerID
df = df.dropna(subset=["CustomerID"])

# Remove exact duplicate records
df = df.drop_duplicates()

# Clean names and cities
for col in ["Name", "City"]:
    df[col] = df[col].astype("string").str.strip().str.title()

# Clean email addresses
df["Email"] = df["Email"].astype("string").str.strip().str.lower()

# Convert numeric columns
df["Age"] = pd.to_numeric(df["Age"], errors="coerce")
df["PurchaseAmount"] = pd.to_numeric(
    df["PurchaseAmount"], errors="coerce"
)

# Fill missing text values
df["Name"] = df["Name"].fillna("Not Provided")
df["Email"] = df["Email"].fillna("Not Provided")
df["City"] = df["City"].fillna("Unknown")

# Fill missing ages using the average
df["Age"] = df["Age"].fillna(round(df["Age"].mean()))

# Keep missing purchase amounts blank

# Save cleaned data
df.to_csv("customer_data_cleaned.csv", index=False)

print("Cleaned rows:", len(df))
print("Final columns:", df.columns.tolist())
print("Missing values:")
print(df.isnull().sum())
print("Cleaned data saved successfully!")
