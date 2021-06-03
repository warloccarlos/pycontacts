#! /usr/bin/python

import sys
from configuration import ConfigMain

c = ConfigMain()

print("Welcome to your Contacts App \n\
 Connect with people you know")

def base():
    act = input("N. New Contact     D. Delete Contact	S. Search Contact     V. View All     0. Exit  ")
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

base()
