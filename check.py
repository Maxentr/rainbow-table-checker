import sys
import csv
from src.db_service import *

if len(sys.argv) != 2:
    print("Usage: python3 insert.py <path to CSV file>")
    sys.exit(1)

path = sys.argv[1]

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
            result = get_password_hashes(row[0])

            if (result is None):
                print("Password: " + row[0] + " not found in the database")
            else:
                print("Password: " + row[0] + " found in the database, " + "MD5: " + result[1] + ", SHA1: " + result[2] + ", SHA256: " + result[3])

                # write to csv file
                writer.writerow([row[0], result[1], result[2], result[3]])
        rainbow_table.close()
