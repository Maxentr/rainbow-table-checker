import sys
import csv
from src.db_service import *

if len(sys.argv) < 2:
    print("Usage: python3 insert.py <path to CSV file>  <column number of password = 0>")
    sys.exit(1)

path = sys.argv[1]

if (len(sys.argv) == 3):
    column = int(sys.argv[2])
else:
    column = 0

# read csv file
with open(path, 'r') as rainbow_table:
    reader = csv.reader(rainbow_table)

    for row in reader:
        insert_password(row[column])

    rainbow_table.close()

print("Done inserting passwords into the database")