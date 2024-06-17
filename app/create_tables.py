import psycopg2

from config import DB_URL

with psycopg2.connect(DB_URL) as conn:
    cursor = conn.cursor()
    cursor.execute(
        'CREATE TABLE defects \
               (id SERIAL PRIMARY KEY,\
               code VARCHAR(50), defect VARCHAR(300),\
               name_of_works VARCHAR(300),\
               measure VARCHAR(300), number INTEGER)',
    )
    cursor.execute(
        'CREATE TABLE employees \
                 (id SERIAL PRIMARY KEY,\
                 employee VARCHAR(200),\
                 surname VARCHAR(50),\
                 name VARCHAR(50),\
                 otchestvo VARCHAR(50),\
                 amount_of_sheets INTEGER)',
    )
