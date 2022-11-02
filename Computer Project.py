from venv import create
import mysql.connector as c
import time
import os
from datetime import date
today=date.today()
cnx=c.connect(host="localhost",user="root",password="root",database="login")
crs=cnx.cursor()
def startup():
    crs.execute("create table if not exists login (Num int(2) primary key AUTO_INCREMENT,User varchar(25),Pass varchar(12))")
    crs.execute("insert ignore into  login values(1,'root','root')")
    crs.execute("create table if not exists crime (Num int(2) primary key AUTO_INCREMENT,crime varchar(25),location varchar(12),Date DATE,description varchar(125),user varchar(25))")
    cnx.commit()
    menu()
def login():
    user=input("Enter your Username: ")
    passs=input("Enter your Password: ")
    crs.execute("select pass from login where user='{}'".format(user))
    check=crs.fetchall()
    for i in check:
        if i[0]==str(passs):
            global x
            x=user
            mainmenu(user)
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
def chngpass(user):
    chng=input("Enter the Password: ")
    print(user)
    crs.execute("update login set Pass='{}' where user='{}'".format(chng,user))
    cnx.commit()
     
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
def mainmenu(user):
    print('\n'*10)
    print('+'*102)
    print() 
    print("MENU".center(185)) 
    print() 
    print("1.Crime Reporting\n2.History\n3.Change Password".center(150))
    print('+'*102)
    r=int(input("Enter your choice: "))
    if r==1:
        crime()
    elif r==2:
        print("History")
    elif r==3:
        print(user)
        chngpass(user)
    else:
        g=input(":")
        print(eval(g))

def crime():
    crime=int(input("TYPES OF CRIMES\n1)TRAFFIC\n2)ASSAULT\n3)THEFT\n4)CYBER\n5)TRAFFICKING\n6)DRUGS\nYOUR CHOICE: "))
    if crime==1:
        crm="traffic"
    elif crime==2:
        crm="assault"
    elif crime==3:
        crm="theft"
    elif crime==4:
        crm="cyber"
    elif crime==5:
        crm="trafficking"
    elif crime==6:
        crm="drugs"
    #os.system('cls')
    loc=input("Enter the location of the crime: ")
    date=today.strftime("%d/%m/%Y")
    desc=input("Enter a description for further evidence: ")
    crs.execute("insert into crime (crime,location,date,description,user) values('{}','{}',now(),'{}','{}')".format(crm,loc,desc,x))
    cnx.commit()



    
startup()
while  True:
    mainmenu(x)
