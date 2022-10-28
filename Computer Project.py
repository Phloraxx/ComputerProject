from venv import create
import mysql.connector as c
cnx=c.connect(host="localhost",user="root",password="root",database="login")
crs=cnx.cursor()
crs.execute("create table if not exists login (Num int(2),User varchar(25),Pass varchar(12))")
cnx.commit()
