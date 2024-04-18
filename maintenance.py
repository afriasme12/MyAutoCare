from aifc import Error
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

def insert_data():
    vehicle = input("What vehicle is it?: ")
    service = input("What service was done?: ")
    date = input ("When was the service done?: ")
    mileage = input("How many miles did the vehicle have when it was done?: ")
    try:      
        sqlresult = conn.execute("INSERT INTO maintenance (vehicle,service,date,mileage)\
            values("+"'"+ str(vehicle) +"'" + ",'"+ str(service) +"', '"+ str(date) +"','"+ str (mileage)+"')")
        result = conn.commit()
        if result == None:
            print("*** Data saved to database. ***")
    except Error as e:
        print ("*** Insert error: ",e)
        pass
def view_data():
    try:
        cursor = conn.execute ("SELECT id,vehicle,service,date,mileage FROM maintenance")
        alldata = []
        alldata.append(["ID","vehicle","service","date","mileage"])
        for row in cursor:
            thisrow=[]
            for x in range(8):
                thisrow.append(row[x])
            alldata.append(thisrow)
        return alldata
    except Error as e:
        print (e)
        pass

def update_data():
    for row in view_data():
            thisrow = "  --> "
            for item in row:
                thisrow += str(item) + "  "
            print (thisrow)
    print('''1 = edit vehicle\n 2 = edit service\n 3 = edit date\n 4 = edit mileage''')
    update_ID = input("Enter the ID of the data record to edit: ")
    feature = input("Enter which feature of the data do you want to edit: ")
    update_value = input ("Editing "+feature+ ": enter the new data: ")

    if(feature == "1"):
        sql = "UPDATE maintenance set vehicle = ? where id =  ?"
    elif (feature == "2"):
       sql = "UPDATE maintenance set service = ? where id =  ?" 
    elif (feature == "3"):
       sql = "UPDATE maintenance set date  = ? where id =  ?"
    elif (feature == "4"):
       sql = "UPDATE maintenance set mileage  = ? where id =  ?"

def delete_data():
    id_  =  input("Enter the ID for the data record to delete:")
    cursor = conn.cursor()
    cursor.execute("select vehicle from maintenance where ID = "+id_)
    delete_item = cursor.fetchall()
    confirm = input("Are you sure you want to delete " + id_ + " " + str(delete_item[0]) + "? (Enter 'y' to confirm.)")
    if confirm.lower() == "y":
        try:
            delete_sql = "DELETE FROM maintenance WHERE id = ?"
            conn.execute(delete_sql,id_)
            result = conn.commit()
            if result == None:
                print (id_ + " " + str(delete_item[0]) + " deleted.")
            else:
                print ("Deletion failed during SQL execution.")
        except Error as e:
            print (e)
            pass
    else:
        print("Deletion aborted.")

while True:
    print("Welcome to MyAutoCare! How may we assist you today?\n 1 = View Vehicle Information\n 2 = Insert new Vehicle Information\n 3 = Update Vehicle Information\n 4 = Delete Vehicle Information\n 5 = Exit")
    name = input ("Choose an operation to perform: ")
    if (name =="1"):
        for row in view_data():
            thisrow = "  --> "
            for item in row:
                thisrow += str(item) + "  "
            print (thisrow)
    elif(name == "2"):
        insert_data()
    elif(name == "3"):
        update_data()
    elif(name == "4"):
        delete_data()
    elif(name == "5"):
        conn.close()
        break