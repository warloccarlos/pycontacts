#! /usr/bin/python

import sys
from createdb import Createdb
from configuration import ConfigMain

c = ConfigMain()
cdb = Createdb()

print("Welcome to your Contacts App \n\
 Connect with people you know")

def base():
    act = input("N. New Contact     D. Delete Contact	S. Search Contact     V. View All     I. Import Contacts      0. Exit  ")
    if act=='N':
        c.saveDetails()
        base()
    elif act=='D':
        c.delDetails()
        base()
    elif act=='S':
        c.searchDetails()
        base()
    elif act=='V':
        c.viewAll()
        base()
    elif act=='I':
        c.import_contacts()
        base()
    elif act=='0':
        print('See ya later!')
        sys.exit(0)
    else:
        print('You chose wrong')
        choice = input('Would you like to try again? Y/N: ')
        if choice == 'Y':
            base()
        else:
            sys.exit(0)

i = cdb.checkdb()

if i ==1:
    base()
else:
    cdb.created()
    base()
