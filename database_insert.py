import psycopg2

conn = psycopg2.connect(
    host='192.168.0.170',
    port=9696,
    dbname='sigaa_ufpb',
    user='postgres'
)

cur = conn.cursor()
cur.execute("select * from aluno")
result = cur.fetchone()
print(result)
