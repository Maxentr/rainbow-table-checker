import hashlib
from src.db import *
from dotenv import dotenv_values

config = dotenv_values(".env")

def get_password_from_hash(hash: str):
    db = get_db()
    cursor = db.cursor()
    cursor.execute('SELECT * FROM ' + config.get("DB_NAME") + ' WHERE md5 = \'{0}\' OR sha1 = \'{0}\' OR sha256 = \'{0}\''.format(hash))

    result = cursor.fetchone()

    cursor.close()
    db.close()

    return result

def get_password_hashes(password: str):
    db = get_db()
    cursor = db.cursor()
    cursor.execute('SELECT * FROM ' + config.get("DB_NAME") + ' WHERE password = \'{0}\''.format(password))

    result = cursor.fetchone()

    cursor.close()
    db.close()

    return result

def password_exist(password: str):
    if (get_password_hashes(password) is None):
        return False
    else:
        return True

def insert_password(password: str):
    encoded_password = password.encode()
    
    if (password_exist(password)):
        print("Password: " + password + " inserted is already in the database")
        return

    md5 = hashlib.md5(encoded_password).hexdigest()
    sha1 = hashlib.sha1(encoded_password).hexdigest()
    sha256 = hashlib.sha256(encoded_password).hexdigest()

    db = get_db()
    cursor = db.cursor()

    cursor.execute("INSERT INTO " + config.get("DB_NAME") + " (password, md5, sha1, sha256) VALUES ('{0}', '{1}', '{2}', '{3}')".format(password, md5, sha1, sha256))

    db.commit()

    cursor.close()
    db.close()

    print("Password: " + password + " inserted successfully")
