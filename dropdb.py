import mysqlconnect
mydb = mysqlconnect.mysqlconnect()

mycursor = mydb.cursor()

mycursor.execute("Drop DATABASE pythonmysql")

