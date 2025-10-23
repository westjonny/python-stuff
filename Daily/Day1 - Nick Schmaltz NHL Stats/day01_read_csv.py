import pandas as pd

# Get file name via input and assign to name
name = input("What is your files path? ")


# Read the CSV file
# df = pd.read_csv('schmaltz_2024-25_game_log.csv')
df = pd.read_csv(name)

# Print basic information
print("=" * 50)
print("DATASET OVERVIEW")
print("=" * 50)

print(f"\nNumber of rows: {len(df)}")
print(f"Number of columns: {len(df.columns)}")
print(f"Shape (rows, columns): {df.shape}")

print("\n" + "=" * 50)
print("COLUMN INFORMATION")
print("=" * 50)
print(f"\nColumn names: {df.columns.tolist()}")
print("\nData types:")
print(df.dtypes)

print("\n" + "=" * 50)
print("DATA PREVIEW")
print("=" * 50)
print(df.head())

print("\n" + "=" * 50)
print("MISSING VALUES")
print("=" * 50)
print(df.isnull().sum())

print("\n" + "=" * 50)
print("NUMERIC STATISTICS")
print("=" * 50)
print(df.describe())
