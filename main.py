#! /usr/bin/python

from configuration import cfgu

c = cfgu()

print("Welcome to your Contacts App to\
 Connect with people you know")
act = input("N. New Contact     D. Delete Contact	S. Search Contact     0. Exit  ")
if act=='N':
    c.saveDetails()
elif act=='D':
    c.delDetails()
elif act=='S':
    c.searchDetails()
elif act=='0':
    exit(0)
else:
    print('You chose wrong')
