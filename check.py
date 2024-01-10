import sys
import csv
from src.db_service import *

if len(sys.argv) < 2:
    print("Usage: python3 insert.py <path to CSV file> <column number of hash = 0>")
    sys.exit(1)

path = sys.argv[1]

if (len(sys.argv) == 3):
    column = int(sys.argv[2])
else:
    column = 0

# remove .csv of path variable
filename = path[:-4]

# read csv file
with open(path, 'r') as rainbow_table:
    reader = csv.reader(rainbow_table)

    with open(filename +'-result.csv', 'w') as rainbow_table:
        writer = csv.writer(rainbow_table)

        for row in reader:
            hash = row[column]
            result = get_password_from_hash(hash)

            if (result is None):
                print("Hash: " + hash + " not found in the database")
            else:
                print("Hash: " + hash + " found in the database, password: " + result[1])

                # write to csv file
                row.append(result[1])
                writer.writerow(row)
        rainbow_table.close()
