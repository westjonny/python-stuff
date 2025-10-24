# Read zip codes from a file
with open('zips.txt', 'r') as file:
    zip_codes = [line.strip() for line in file]

# Clean zip codes: remove trailing 4 digits and pad with leading zeros
cleaned_zips = []
for zip_code in zip_codes:
    # Remove the trailing 4 digits
    base_zip = zip_code.split('-')[0]
    # Pad with leading zeros to ensure 5 digits
    base_zip = base_zip.zfill(5)
    cleaned_zips.append(base_zip)

# Remove duplicates while preserving order
unique_zips = list(dict.fromkeys(cleaned_zips))

# Write unique zip codes to a new file
with open('unique_zip_codes.txt', 'w') as file:
    for zip_code in unique_zips:
        file.write(zip_code + '\n')

print(f"Original count: {len(zip_codes)}")
print(f"Unique count: {len(unique_zips)}")
print(f"Duplicates removed: {len(zip_codes) - len(unique_zips)}")