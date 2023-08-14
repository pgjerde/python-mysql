import mysqlconnect 

mydb = mysqlconnect.mysqlconnect('pythonmysql')

mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")
