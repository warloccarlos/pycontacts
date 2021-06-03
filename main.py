#! /usr/bin/python

import sys
from configuration import cfgu

c = ConfigMain()

print("Welcome to your Contacts App \n\
 Connect with people you know")
act = input("N. New Contact     D. Delete Contact	S. Search Contact     V. View All     0. Exit  ")
if act=='N':
    c.saveDetails()
elif act=='D':
    c.delDetails()
elif act=='S':
    c.searchDetails()
elif act=='V':
    c.viewAll()
elif act=='0':
    print('See ya later!')
    sys.exit(0)
else:
    print('You chose wrong')
