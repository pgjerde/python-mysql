import mysqlconnect
mydb = mysqlconnect.mysqlconnect()

mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE pythonmysql")

