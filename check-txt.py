import sys
from src.db_service import *

if len(sys.argv) < 1:
    print("Usage: python3 check-txt.py <path to CSV file> <column number of hash = 0> <separator = :>")
    sys.exit(1)

path = sys.argv[1]

if (len(sys.argv) == 3):
    column = int(sys.argv[2])
else:
    column = 0

if (len(sys.argv) == 4):
    separator = int(sys.argv[3])
else:
    separator = ':'

# remove .txt of path variable
filename = path[:-4]

# read txt file
with open(path, 'r') as rainbow_table:
    with open(filename +'-result.txt', 'w') as result_file:
        for line in rainbow_table:
            line_array = line.split(separator)
            hash = line_array[column]
            result = get_password_from_hash(hash)

            if (result is None):
                print("Hash: " + hash + " not found in the database")
            else:
                print("Hash: " + hash + " found in the database, password: " + result[1])

                # write to txt file
                line_array.append(result[1])
                result_file.write(separator.join(line_array))
        result_file.close()