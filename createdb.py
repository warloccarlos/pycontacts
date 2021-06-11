import mysql.connector
import config as cfg

class Createdb:
    global i

    def checkdb(self):
        try:
            con = mysql.connector.connect(host=cfg.sql['host'], user=cfg.sql['user'], \
            password=cfg.sql['password'], port=cfg.sql['port'])
            cur = con.cursor()
            cur.execute("show databases")
            dblist = cur.fetchall()
            for l in dblist:
                if l == 'contacts':
                    self.i = self.i + 1
            return 1
        except Exception as e:
            print(e)

    def created(self):
        self.i = 0
        try:
            con = mysql.connector.connect(host=cfg.sql['host'], user=cfg.sql['user'], \
            password=cfg.sql['password'], port=cfg.sql['port'])
            cur = con.cursor()
            cur.execute("create database contacts")
            cur.execute("create table contacts.connections(id int AUTO_INCREMENT NOT NULL, fname text NOT NULL,\
             lname TEXT NULL, company TEXT NULL, mobile TEXT NOT NULL, email TEXT NULL)")
            con.commit()
            if cur.rowcount == 0:
                print("Database created with table")
                self.i = 1
                return 1
        except Exception as e:
            print(e)
