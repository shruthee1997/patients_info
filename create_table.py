import psycopg2
conn = psycopg2.connect(
   database="patients", user='postgres', password='root', host='127.0.0.1', port= '5432'
)

cursor = conn.cursor()
create_table_query = '''
    CREATE TABLE patients (
        id SERIAL PRIMARY KEY,
        name TEXT NOT NULL,
        dob TEXT NOT NULL,
        gender TEXT NOT NULL,
        mobile TEXT NOT NULL
    )
'''
cursor.execute(create_table_query)
conn.commit()
conn.close()

