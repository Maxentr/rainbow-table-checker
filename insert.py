import sys
import csv
from src.db_service import *

if len(sys.argv) != 2:
    print("Usage: python3 insert.py <path to CSV file>")
    sys.exit(1)

path = sys.argv[1]

# read csv file
with open(path, 'r') as rainbow_table:
    reader = csv.reader(rainbow_table)

    for row in reader:
        insert_password(row[0])

