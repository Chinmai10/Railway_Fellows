import mysql.connector

dataBase = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="password123",
    
)
cursorObeject = dataBase.cursor()

cursorObeject.execute("CREATE DATABASE trains_db")

print("all done!!")