import pandas as pd

#Read the .csv file
df = pd.read_csv('customers.csv')


#Checking .csv 
print("=" * 22, 'START', '=' * 22)
print("Orignial Dataset:")
print(df)
print(f"\nRow Count: {len(df)}")


#Filtering to Utah Customers only
utah_customers = df[df['state'] == 'UT']

print("=" * 50)
print("\nFinding only customers in Utah:")
print(utah_customers)
print(f"Row Count: {len(utah_customers)}")

#Filtering to Utah or California Customers
ut_ca_customers = df[(df['state'] == 'UT') | (df['state'] == 'CA')]
#Could also be written using .isin():
# ut_ca_customers = df[df['state'].isin(['UT', 'CA'])]


print("=" * 50)
print("\nFinding only customers in Utah OR California:")
print(ut_ca_customers)
print(f"Row Count: {len(ut_ca_customers)}")

#Filtering to customers with > 1,000 in ltv
high_ltv_utah = df[(df['state'] == 'UT') & (df['lifetime_value'] >= 1000)]

print("=" * 50)
print("\nFinding only customers in Utah who have a lifetime value of greater than or equal to $1,000:")
print(high_ltv_utah)
print(f"Row Count: {len(high_ltv_utah)}")


#Handling Null values
high_value_utah_clean = df[
    (df['state'] == 'UT') &
    (df['lifetime_value'] >= 1000) &
    (df['lifetime_value'].notna()) #Excludes missing values
]

print("=" * 50)
print("\nHigh values customers, from utah, excluding null lifetime values:")
print(high_value_utah_clean)
print("=" * 23, 'END', '=' * 23)


#Exporting filtered data as new .csv
#Defininig out put file name
output_file = 'high_value_utah_clean.csv'

#Writing to .csv
high_value_utah_clean.to_csv(output_file, index=False)

print("\n✅ Filtered data saved to: {output_file}")
print(f"Rows exported: {len(high_value_utah_clean)}")