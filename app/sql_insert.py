import psycopg2
import os

print("Data Inserting...")

conn = psycopg2.connect(
    host='db',
    port=os.environ.get('DB_PORT'),
    user=os.environ.get('DB_USER'),
    password=os.environ.get('DB_PASS'),
    database='postgres'
)

conn.autocommit = True
cursor = conn.cursor()

with open('sql_insert.sql', 'r') as f:
    sql = f.read()

cursor.execute(sql)
print("Data Inserted")
conn.close()
