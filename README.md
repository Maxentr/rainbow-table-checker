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

### Check a hash

```
python3 check.py <path to CSV file> <column number of password = 0>
```
