import os, sys, time, subprocess


def adduser():
    users =  {
        "root": "root",
        "pikachu": "password",
        "admin": "admin"
    }
        
    usertoadd = input("Enter Username: ")
    usertoaddpass = input(f"Enter Password for {usertoadd}: ")
    planlength = input(f'Enter time for {usertoadd}\'s plan: ')
    planchoice = input(f'Enter permisions for {usertoadd}: ')
        
    users = {
        "root": "root",
        "pikachu": "password",
        "admin": "admin",
        usertoadd: usertoaddpass 
    }
    print(users)

adduser()