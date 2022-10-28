from venv import create
import mysql.connector as c
cnx=c.connect(host="localhost",user="root",password="root",database="login")
crs=cnx.cursor()
def startup():
    crs.execute("show tables like 'login'")
    x=crs.fetchall()
    for i in x:
        print(i)
    if x==[]:
        print("yes")
        crs.execute("create table login (Num int(2),User varchar(25),Pass varchar(12))")
        crs.execute("insert into login values(1,'root','root')")
startup()
cnx.commit()
