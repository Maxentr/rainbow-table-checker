import psycopg2
from dotenv import dotenv_values

config = dotenv_values(".env")


def get_db():
    return psycopg2.connect(
        host=config.get("DB_HOST"),
        database=config.get("DB_NAME"),
        user=config.get("DB_USER"),
        password=config.get("DB_PASSWORD"))