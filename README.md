# Rainbow table in CSV

## Requirements

- Python 3.6 or higher
- Pip
- postgresql database

## Installation

```
pip install -r requirements.txt
```

Copy `.env.example` to `.env` and fill the variables.

## Presentation

This project allows you to check `md5`, `sha1` and `sha256` hashes from a rainbow table.
The CSV has to be formatted as follow:

```
password
```

You can either check passwords or save passwords in the rainbow table.

## Usage

### Insert password in the database

```
python3 insert.py <path to CSV file> <column number of password = 0>
```

### Check a password from its hash

These functions will print the hash and password if it is found and will add the row/object to `filename-result.{csv,txt,json}`.

#### CSV files

```
python3 check.py <path to CSV file> <column number of hash = 0>
```

#### TXT files

```
python3 check-txt.py <path to TXT file> <column number of hash = 0> <separator = :>
```

#### Json files

```
python3 check-json.json <path to Json file> <column number of hash = 0>
```
