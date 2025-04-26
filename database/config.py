import os

# URL de conexão com o PostgreSQL
POSTGRES = {
    'user': 'postgres',
    'pw': '1234',
    'db': 'loginsite',
    'host': 'localhost',
    'port': '5432',
}

SQLALCHEMY_DATABASE_URI = f"postgresql://{POSTGRES['user']}:{POSTGRES['pw']}@{POSTGRES['host']}:{POSTGRES['port']}/{POSTGRES['db']}"
SQLALCHEMY_TRACK_MODIFICATIONS = False