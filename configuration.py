#! /usr/bin/python

import csv
import mysql.connector
import config as cfg

class ConfigMain:
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
            query = "insert into connections(fname, lname, company, mobile, email)\
             values(%s, %s, %s, %s, %s);"
            cur.execute(query, val)
            con.commit()
            if cur.rowcount ==1:
                print("Details saved.")
            else:
                print("Details not saved.")
            con.close()
        except Exception as e:
            print(e)

    def delDetails(self):
        try:
            con = mysql.connector.connect(host=cfg.sql['host'], user=cfg.sql['user'], \
            password=cfg.sql['password'], database=cfg.sql['database'], port=cfg.sql['port'])
            cur = con.cursor()
            name = input("First Name that you want to delete: ")
            query = "delete from connections where fname=%s;"
            cur.execute(query, (name,))
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
            query = "select * from connections where fname=%s;"
            cur.execute(query, (name,))
            rs = cur.fetchone()
            print(rs)
            con.close()
        except Exception as e:
            print(e)

    def viewAll(self):
        try:
            con = mysql.connector.connect(host=cfg.sql['host'], user=cfg.sql['user'], \
            password=cfg.sql['password'], database=cfg.sql['database'], port=cfg.sql['port'])
            cur = con.cursor()
            query = "select * from connections;"
            cur.execute(query)
            rs = cur.fetchall()
            for r in rs:
                print(r)
            con.close()
        except Exception as e:
            print(e)

    def import_contacts(self):
        try:
            print("For initial release, only CSV are supported")
            file = input("Please provide the name of file with path to import: ")
            con = mysql.connector.connect(host=cfg.sql['host'], user=cfg.sql['user'], \
            password=cfg.sql['password'], database=cfg.sql['database'], port=cfg.sql['port'])
            cur = con.cursor()
            with open(file) as csv_file:
                csv_reader = csv.reader(csv_file, delimiter=',')
                line_count = 0
                for row in csv_reader:
                    fname = row[1]
                    lname = row[2]
                    company = row[3]
                    mobile = row[4]
                    email = row[5]
                    val = (fname, lname, company, mobile, email)
                    query = "insert into connections(fname, lname, company, mobile, email)\
                     values(%s, %s, %s, %s, %s);"
                    cur.execute(query, val)
                    con.commit()
                    if cur.rowcount ==1:
                        print("Details saved.")
                    else:
                        print("Details not saved.")
                    line_count += 1
                con.close()
                print(f'Contacts Processed {line_count}.')
        except Exception as e:
            print(e)
