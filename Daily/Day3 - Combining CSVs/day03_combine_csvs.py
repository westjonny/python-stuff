import pandas as pd
import os
from pathlib import Path

##Old Standard - using OS

# # Creating an empty list to store the DataFrames
# dataframes = []

# # Defining the folder containing our data, to be used in creating path name later
# data_folder = 'data'

# # Listing all files within the containing folder 
# all_files = os.listdir(data_folder)

# # Filtering for only CSV files 
# csv_files = [f for f in all_files if f.endswith('.csv')]

# print("=" * 20, 'START', "=" * 20)
# print(f"CSV files found in directory: {len(csv_files)}")
# for file in csv_files: #file is assigning an alias to the elements within csv_files list
#     print(f" - {file}")

# # Loop through each file within the list
# for file in csv_files:
#     # Build full file path
#     file_path = os.path.join(data_folder, file)
#     print(f"reading: {file_path}")
    
#     # Read CSV into DataFrame
#     df = pd.read_csv(file_path)

#     df['source_file'] = file

#     # Adding CSV df to previously created list
#     dataframes.append(df)

#     print(f"Rows: {len(df)}")

# print(f"Total DataFrames loaded: {len(dataframes)}")
# print("\nPre-concat dataframes(seperate indexing, dupe column names):")
# print(dataframes)

# # Combine all DataFrames into one
# combined_df = pd.concat(dataframes, ignore_index=True)

# print("\nCombined DataFrame:")
# print(combined_df)
# print(f"\nTotal rows: {len(combined_df)}")
# print(f"Total columns: {len(combined_df.columns)}")


##New Standard - Using pathlib

# Define folder as Path object 
data_folder = Path('data')

# Get all .csv files 
csv_files = list(data_folder.glob('*.csv'))

print('=' * 20, 'START', '=' * 20)
print(f"CSV files found: {len(csv_files)}")

# Creating empty lists
dataframes = []
failed_files = []

for file_path in csv_files:
    try:
        print(f"Reading: {file_path.name}")
        df = pd.read_csv(file_path)
        df['source_file'] = file_path.name
        dataframes.append(df)
        print(f"✅ Success - {len(df)} rows")
    except Exception as e:
        print(f" ❌ Failed - {e}")
        failed_files.append(file_path.name)

# Only combining if we have data
if dataframes:
    combine_df = pd.concat(dataframes, ignore_index = True)

    # Save to new CSV
    output_file = 'combined_services_october.csv'
    combine_df.to_csv(output_file, index=False)

    print('=' * 47)   
    print('EXPORT COMPLETE') 
    print('=' * 47)
    print('EXPORT RESULTS')
    print(combine_df)
    print(f"✅ Combined data saved to: {output_file}")
    print(f"📊 Total rows exported: {len(combine_df)}")
    print(f"📁 Source files: {len(dataframes)}")
    print('=' * 21, 'END', '=' * 21)
else:
    print("\n⚠️  No data to combine!")

# Report any failures
if failed_files:
    print(f"\n⚠️  Failed to read {len(failed_files)} files:")
    for file in failed_files:
        print(f"  - {file}")