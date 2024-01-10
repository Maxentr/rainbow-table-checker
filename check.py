import sys
import csv
from src.db_service import *

if len(sys.argv) < 2:
    print("Usage: python3 insert.py <path to CSV file> <column number of password = 0>")
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
        writer.writerow(['password', 'md5', 'sha1', 'sha256'])

        # check if password is in the database
        for row in reader:
            result = get_password_hashes(row[column])

            if (result is None):
                print("Password: " + result[1] + " not found in the database")
            else:
                print("Password: " + result[1] + " found in the database, " + "MD5: " + result[2] + ", SHA1: " + result[3] + ", SHA256: " + result[4])

                # write to csv file
                writer.writerow([result[1], result[2], result[3], result[4]])
        rainbow_table.close()
