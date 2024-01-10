import sys
import json
from src.db_service import *
import io

if len(sys.argv) < 1:
    print("Usage: python3 check-json.py <path to json file> <object key name of hash = 'password'>")
    sys.exit(1)

path = sys.argv[1]

if (len(sys.argv) == 3):
    key = str(sys.argv[2])
else:
    key = 'password'

# remove .txt of path variable
filename = path[:-5]

# read txt file
with open(path, 'r') as rainbow_table:
        loaded_json = json.load(rainbow_table)
        result_json = list()

        for item in loaded_json:
            hash: str = item[key]
            result = get_password_from_hash(hash)

            if (result is None):
                print("Hash: " + hash + " not found in the database")
            else:
                print("Hash: " + hash + " found in the database, password: " + result[1])

                # write to txt file
                item["deciphered_password"] = result[1]
                result_json.append(item)

        # write to json file
        with open(filename +'-result.json', 'w', encoding='utf8') as result_file:
            str_ = json.dumps(result_json,
                      indent=4, sort_keys=True,
                      separators=(',', ': '), ensure_ascii=False)
            result_file.write(str_)