'''import mysql.connector
#import mysqldb

def fetch():
    try:
        con = mysql.connector.connect(host="localhost", user="root", password="", database="contacts", port="3308")
        #con = mysqldb.connect(host="localhost", user="root", password="", database="contacts", port="3308")
        cur = con.cursor()
        cur.execute("select * from connections")
        rs = cur.fetchall()
        for x in rs:
            print(x)
    except Exception as e:
        print(e)


fetch()


class z:
    global name
    def inp(self):
        self.name = input("Enter anything: ")
    def show(self):
        print(self.name)
a = z()
#a.inp()
#a.show()

def fetch():
    try:
        con = mysql.connector.connect(host='localhost', user='root', password='StoneCold', database='contacts')
        cur = con.cursor()
        name = input("First Name that you want to search: ")
        val  = (name)
        query = "select * from connections where fname='%s';"
        #cur.execute(query, val)
        cur.execute("select * from connections where fname='"+val+"';")
        rs = cur.fetchone()
        print(rs)
        for r in rs:
            print(r)
        con.close()
    except Exception as e:
        print(e)

fetch()
'''

ch = input("Enter Y/N: ")
switcher={
    'Y':'Yes',
    'N':'No'
}
c = switcher.get(ch, "Choose correct")
print(c)
