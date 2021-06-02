#! /usr/bin/python

import mysql.connector
import config as cfg

class cfgu:
    global fname, lname, company, mobile, email

    def saveDetails(self):
        self.fname = input("First Name: ")
        self.lname = input("Last Name: ")
        self.company = input("Comapnmy: ")
        self.mobile = input("Mobile: ")
        self.email = input("Email: ")
        try:
            con = mysql.connector.connect(host=cfg.sql['host'], user=cfg.sql['user'], \
            password=cfg.sql['password'], database=cfg.sql['database'], port=cfg.sql['port'])
            cur = con.cursor()
            val = (self.fname, self.lname, self.company, self.mobile, self.email)
            query = "insert into connections(fname, lname, company, mobile, email) values(%s, %s, %s, %s, %s);"
            cur.execute(query, val)
            con.commit()
            if cur.rowcount ==1:
                print("Details saved.")
                return 1
            else:
                print("Details not saved.")
                return 0
            con.close()
        except Exception as e:
            print(e)

    def delDetails(self):
        try:
            con = mysql.connector.connect(host=cfg.sql['host'], user=cfg.sql['user'], \
            password=cfg.sql['password'], database=cfg.sql['database'], port=cfg.sql['port'])
            cur = con.cursor()
            name = input("First Name that you want to delete: ")
            query = "delete from connections where fname='"+name+"';"
            cur.execute(query)
            con.commit()
            if cur.rowcount == 1:
                print("Detail deleted.")
                return 1
            else:
                print("Detail not deleted.")
                return 0
            con.close()
        except Exception as e:
            print(e)

    def searchDetails(self):
        try:
            con = mysql.connector.connect(host=cfg.sql['host'], user=cfg.sql['user'], \
            password=cfg.sql['password'], database=cfg.sql['database'], port=cfg.sql['port'])
            cur = con.cursor()
            name = input("First Name that you want to search: ")
            query = "select * from connections where fname='"+name+"';"
            cur.execute(query)
            rs = cur.fetchone()
            print(rs)
            con.close()
        except Exception as e:
            print(e)