from venv import create
import mysql.connector as c
import time
import os
from datetime import date
today=date.today()
cnx=c.connect(host="localhost",user="root",password="root",database="login")
crs=cnx.cursor()
def startup():
    crs.execute("create table if not exists login (Num int(2) primary key AUTO_INCREMENT,User varchar(25),Pass varchar(12),Phoneno int(10),Admin varchar(1))")
    crs.execute("insert ignore into  login values(1,'root','root',100,'y')")
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
    os.system('CLS')
    user=input("Enter your Username: ")
    print()
    passs=input("Enter your Password: ")
    print()
    pass_check=input("ReEnter your Password: ")
    print()
    phno=int(input("Enter your Phone Number: "))
    ad="n"
    if passs==pass_check:
        crs.execute("insert into login (user,pass,phoneno,admin) values('{}','{}',{},'{}')".format(user,passs,phno,ad))
        cnx.commit()
        os.system('CLS')
        print("Registering....")
        time.sleep(3)
        print("Registered Successfully!")
        menu()
    else:
        os.system('CLS')
        print("Recheck Failed, Retry!")
        time.sleep(2)
        register()
def chngpass(user):
        os.system('CLS')
        usr=input("Enter the Password: ")
        crs.execute("update login set pass='{}' where user='{}'".format(usr,x))
        cnx.commit()
        os.system('CLS')
        print("Changing Password.....")
        time.sleep(1)
        print("Successfully Changed!")
        time.sleep(2)
     
def menu():
    os.system('CLS')
    print('\n'*10)
    print('+'*25)
    print() 
    print("MENU".center(25)) 
    print('-'*25)
    print() 
    print("1.Login(Sign IN)\n".center(12))
    print("2.Register(Sign UP)           (3.exit)".center(12))
    print('+'*25)
    while True:
        try:
            r=int(input("Enter your choice: "))
            break
        except ValueError:
            os.system('CLS')
            print("Errored!.   Reconnecting....")
            time.sleep(2)
            menu()
    if r==1:
        login()
    elif r==2:
        register()
    elif r==3:
        os.system('CLS')
        print("Call 100 For Further Assistance")
        time.sleep(2)
        os.system('CLS')
        exit()
    else:
        print("Returning to menu.....")
        time.sleep(3)
        menu()
def mainmenu(user=7):
    crs.execute("select admin from login where user='{}'".format(user))
    check=crs.fetchall()
    if user==7:
        menu()
    os.system('cls')
    print("Logging in!")
    time.sleep(1)
    os.system('cls')
    print('\n'*10)
    print('+'*25)
    print() 
    print("MAINMENU".center(25)) 
    print('-'*25)
    print() 
    print("1.Crime Reporting\n\n2.History\n\n3.Change Password\n\n4.Logout")
    for i in check:
        if i[0]=="y":
            print("\n5.Admin Menu")
    print('+'*25)
    while True:
        try:
            r=int(input("Enter your choice: "))
            break
        except ValueError:
            os.system('CLS')
            print("Errored!.   Reconnecting....")
            time.sleep(2)
            mainmenu(user)
    if r==1:
        crime()
    elif r==2:
        print("History")
    elif r==3:
        print(user)
        chngpass(user)
    elif r==4:
        print("Logging Out!....")
        global x
        del x
        time.sleep(3)
        menu()
    elif r==5:
        for i in check:
            if i[0]=="y":
                admin()
    else:
        mainmenu(x)

def crime():
    os.system('CLS')
    print('\n'*10)
    print('+'*25)
    print() 
    print("TYPES OF CRIMES".center(25))
    print('-'*25)
    print("1.TRAFFIC\n\n2.ASSAULT\n\n3.THEFT\n\n4.CYBER\n\n5.TRAFFICKING\n\n6.DRUGS")
    print('+'*25)
    while True:
        try:
            crime=int(input("Enter your choice: "))
            break
        except ValueError:
            os.system('CLS')
            print("Errored!.   Reconnecting....")
            time.sleep(2)
            mainmenu(x)
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
    print()
    loc=input("Enter the location of the crime: ")
    date=today.strftime("%d/%m/%Y")
    print()
    desc=input("Enter a description for further evidence: ")
    crs.execute("insert into crime (crime,location,date,description,user) values('{}','{}',now(),'{}','{}')".format(crm,loc,desc,x))
    cnx.commit()
    os.system('cls')
    print("Reporting Crime ....")
    time.sleep(2)
    os.system('cls')
    print("Thank You For Your Service!")
    time.sleep(3)
    mainmenu(x)
def admin():
    os.system('cls')
    print("Logging in!")
    time.sleep(1)
    os.system('cls')
    print('\n'*10)
    print('+'*25)
    print() 
    print("ADMIN MENU".center(25))
    print('-'*25)
    print("1.USER DATA\n\n2.CRIME DATA")
    print('+'*25)
    while True:
        try:
            r=int(input("Enter your choice: "))
            break
        except ValueError:
            os.system('CLS')
            print("Errored!.   Reconnecting....")
            time.sleep(2)
            mainmenu(x)
    if r==1:
        userdata()
    if r==2:
        crimedata()
    else:
        mainmenu(x)

def userdata():
    print('\n'*10)
    print('+'*25)
    print() 
    print("USER DATA".center(25))
    print('-'*25)
    print("1.SHOW ALL USERS\n\n2.SEARCH BY USERNAME\n\n3.SEARCH BY PHONE NO\n\n4.CHANGE USERDATA")
    print('+'*25)
    while True:
        try:
            r=int(input("Enter your choice: "))
            break
        except ValueError:
            os.system('CLS')
            print("Errored!.   Reconnecting....")
            time.sleep(2)
            userdata()
    if r==1:
        crs.execute("select * from login")
        check=crs.fetchall()
        print("+--------------------------+\n")
        for i in check:
            print(" | User Number  : ",i[0],"\n | User Name    : ",i[1],"\n | Phone Number : ",i[3],"\n | Admin        : ",i[4],"\n")
            print("+--------------------------+\n")
        c=input("Enter To Continue")
        userdata()
    elif r==2:
        c=input("Enter the UserName to search: ")
        crs.execute("select * from login where user='{}'".format(c))
        check=crs.fetchall()
        print("+--------------------------+\n")
        for i in check:
            print(" | User Number  : ",i[0],"\n | User Name    : ",i[1],"\n | Phone Number : ",i[3],"\n | Admin        : ",i[4],"\n")
            print("+--------------------------+\n")
        c=input("Enter To Continue")
        userdata()
    elif r==3:
        c=input("Enter the Phone No to search: ")
        crs.execute("select * from login where phoneno={}".format(c))
        check=crs.fetchall()
        print("+--------------------------+\n")
        for i in check:
            print(" | User Number  : ",i[0],"\n | User Name    : ",i[1],"\n | Phone Number : ",i[3],"\n | Admin        : ",i[4],"\n")
            print("+--------------------------+\n")
        c=input("Enter To Continue")
        userdata()
    elif r==4:
        print('\n'*10)
        print('+'*25)
        print() 
        print("USER DATA".center(25))
        print('-'*25)
        print("1.CHANGE USERNAME\n\n2.CHANGE PASSWORD\n\n3.CHANGE ADMIN PRIVILAGES\n\n4.DELETE USER")
        print('+'*25)
        while True:
            try:
                k=int(input("Enter your choice: "))
                break
            except ValueError:
                os.system('CLS')
                print("Errored!.   Reconnecting....")
                time.sleep(2)
                userdata()
        if k==1:
            os.system('CLS')
            chng=input("Enter the User to change: ")
            print()
            usr=input("Enter the UserName: ")
            crs.execute("update login set user='{}' where user='{}'".format(usr,chng))
            cnx.commit()
            os.system('CLS')
            print("Changing UserName.....")
            time.sleep(1)
            print("Successfully Changed!")
            time.sleep(2)
        elif k==2:
            os.system('CLS')
            chng=input("Enter the User to change: ")
            print()
            usr=input("Enter the Password: ")
            crs.execute("update login set pass='{}' where user='{}'".format(usr,chng))
            cnx.commit()
            os.system('CLS')
            print("Changing Password.....")
            time.sleep(1)
            print("Successfully Changed!")
            time.sleep(2)
        elif k==3:
            os.system('CLS')
            chng=input("Enter the User to change: ")
            print()
            usr=input("Change Admin Privilages: ")
            crs.execute("update login set admin='{}' where user='{}'".format(usr,chng))
            cnx.commit()
            os.system('CLS')
            print("Changing Privilages.....")
            time.sleep(1)
            print("Successfully Changed!")
            time.sleep(2)
        elif k==4:
            os.system('CLS')
            chng=input("Enter the User to DELETE: ")
            print()
            crs.execute("delete from login where user='{}'".format(chng))
            cnx.commit()
            os.system('CLS')
            print("Deleting User.....")
            time.sleep(1)
            print("Successfully Deleted!")
            time.sleep(2)         
        else:
            userdata() 
    else:
        admin()
def crimedata():  
    print('\n'*10)
    print('+'*25)
    print() 
    print("USER DATA".center(25))
    print('-'*25)
    print("1.SHOW ALL REPORTS\n\n2.SEARCH BY CRIME\n\n3.SEARCH BY USER\n\n4.SEARCH BY CRIME NUMBER")
    print('+'*25)
    while True:
        try:
            k=int(input("Enter your choice: "))
            break
        except ValueError:
            os.system('CLS')
            print("Errored!.   Reconnecting....")
            time.sleep(2)
            crimedata()
    if k==1:
        crs.execute("select * from crime")
        check=crs.fetchall()
        print("+--------------------------------+\n")
        for i in check:
            print(" | Crime Number    : ",i[0],"\n | Crime           : ",i[1],"\n | Location        : ",i[2],"\n | Date            : ",i[3],"\n | Description     : ",i[4],"\n | User Reported   : ",i[5],"\n")
            print("+--------------------------------+\n")
        c=input("Enter To Continue")
        crimedata()
    elif k==2:
        c=input("Enter the Crime to search: ")
        crs.execute("select * from crime where crime='{}'".format(c))
        check=crs.fetchall()
        print("+--------------------------------+\n")
        for i in check:
            print(" | Crime Number    : ",i[0],"\n | Crime           : ",i[1],"\n | Location        : ",i[2],"\n | Date            : ",i[3],"\n | Description     : ",i[4],"\n | User Reported   : ",i[5],"\n")
            print("+--------------------------------+\n")
        c=input("Enter To Continue")
        crimedata()
    elif k==3:
        c=input("Enter the User to search: ")
        crs.execute("select * from crime where user='{}'".format(c))
        check=crs.fetchall()
        print("+--------------------------------+\n")
        for i in check:
            print(" | Crime Number    : ",i[0],"\n | Crime           : ",i[1],"\n | Location        : ",i[2],"\n | Date            : ",i[3],"\n | Description     : ",i[4],"\n | User Reported   : ",i[5],"\n")
            print("+--------------------------------+\n")
        c=input("Enter To Continue")
        crimedata()
    elif k==4:
        c=input("Enter the Crime Number to search: ")
        crs.execute("select * from crime where num='{}'".format(c))
        check=crs.fetchall()
        print("+--------------------------------+\n")
        for i in check:
            print(" | Crime Number    : ",i[0],"\n | Crime           : ",i[1],"\n | Location        : ",i[2],"\n | Date            : ",i[3],"\n | Description     : ",i[4],"\n | User Reported   : ",i[5],"\n")
            print("+--------------------------------+\n")
        c=input("Enter To Continue")
        crimedata()
    else:
        crimedata()

    



    
    

    
startup()
while  True:
    try:
        x
        time.sleep(3)
        mainmenu(x)
    except NameError:
        time.sleep(3)
        menu()
