import csv

# Change this to your actual file name if different
csv_file = 'casino_users.csv'

with open(csv_file, mode='r', encoding='utf-8-sig') as file:
    reader = csv.reader(file)
    next(reader, None)  # Skip the header
    row_count = sum(1 for _ in reader)

print(f"Number of data rows (excluding header): {row_count}")
