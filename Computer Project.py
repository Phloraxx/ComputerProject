from venv import create
import mysql.connector as c
cnx=c.connect(host="localhost",user="root",password="root",database="login")
crs=cnx.cursor()
def startup():
    crs.execute("create table if not exists login (Num int(2) primary key,User varchar(25),Pass varchar(12))")
    crs.execute("insert ignore into  login values(1,'root','root')")
    cnx.commit()
startup()
user=input("Enter your Username: ")
passs=input("Enter your Password: ")
crs.execute("select pass from login where user='{}'".format(user))
check=crs.fetchall()
for i in check:
 if i[0]==str(passs):
    menu()
   
