import sqlite3

conn = sqlite3.connect('automtc.ed')

c=conn.cursor()

c.execute("""CREATE TABLE maintenance (
          vehicle text,
          service_type text,
          service_date text
          )""")

conn.commit()

conn.close()