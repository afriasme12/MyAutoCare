import sqlite3

conn = sqlite3.connect('automtc.ed')

c=conn.cursor()

sql_query = """SELECT name FROM sqlite_master WHERE type='table';"""
c.execute(sql_query)
results = c.fetchall()
results_list = [item[0] for item in results]
for x in results_list:
    if 'maintenance' in results_list:
        pass
    else:
        c.execute("""CREATE TABLE maintenance (
                vehicle text,
                service_type text,
                service_date text
                )""")

conn.commit()

conn.close()

autointro = input ("Hello and welcome to MyAutoCare! How may we assist you today?\n 1 = View current maintenance page\n 2 = Update maintenance page\n 3 = Recieve maintenance recommendations\n 4 = Exit\n")