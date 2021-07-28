import mysql.connector

db_con = mysql.connector.connect(
    host='',
    user='',
    passwd='',
    database=''
)

cursor = db_con.cursor()

db_con.commit()