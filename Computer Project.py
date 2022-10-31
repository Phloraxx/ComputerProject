from venv import create
import mysql.connector as c
import time
cnx=c.connect(host="localhost",user="root",password="root",database="login")
crs=cnx.cursor()
def startup():
    crs.execute("create table if not exists login (Num int(2) primary key AUTO_INCREMENT,User varchar(25),Pass varchar(12))")
    crs.execute("insert ignore into  login values(1,'root','root')")
    cnx.commit()
    menu()
def login():
    user=input("Enter your Username: ")
    passs=input("Enter your Password: ")
    crs.execute("select pass from login where user='{}'".format(user))
    check=crs.fetchall()
    for i in check:
        if i[0]==str(passs):
            print("k")
def register():
    user=input("Enter your Username: ")
    passs=input("Enter your Password: ")
    pass_check=input("ReEnter your Password: ")
    if passs==pass_check:
        crs.execute("insert into login (user,pass) values('{}','{}')".format(user,passs))
        print("yes")
        cnx.commit()
    else:
        print("Recheck Failed, Retry!")
        register()
     
def menu():
    print('\n'*10)
    print('+'*102)
    print() 
    print("MENU".center(185)) 
    print() 
    print("1.Login(Sign IN)".center(150),"2.Register(Sign UP)".center(150))
    print('+'*102)
    r=int(input("Enter your choice: "))
    if r==1:
        login()
    elif r==2:
        register()
    else:
        print("Returning to menu.....")
        time.sleep(3)
        menu()
startup()
