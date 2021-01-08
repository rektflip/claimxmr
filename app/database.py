import sqlite3
import os


class Database_cl(object):
    def __init__(self):
        self.dbpath = os.path.join(os.path.dirname(__file__) + "database.sqlite3")
        self.connection = self.db_connect(self.dbpath)
        self.cur = self.connection.cursor()

    def db_connect(self, db_path):
        con = sqlite3.connect(db_path, check_same_thread=False)
        return con

    def createTable(self):
        links_sql = "CREATE TABLE claims (ID INTEGER PRIMARY KEY, subadr text NOT NULL)"
        self.cur.execute(links_sql)

    # SQLInjection!!!
    def insertEntry(self, ID, subadr):
        link_sql = "INSERT INTO claims (ID, subadr) VALUES (?, ?)"
        self.cur.execute(link_sql, (str(ID), str(subadr)))
        self.connection.commit()

    def getDB(self):
        self.cur.execute("SELECT * FROM claims")
        return self.cur.fetchall()

    # SQLInjection!!!
    def getID(self, subadr):
        self.cur.execute('SELECT ID FROM claims WHERE subadr = "' + str(subadr) + '"')
        return self.cur.fetchall()[0][0]

    # SQLInjection!!!
    def deleteEntry(self, ID):
        link_sql = "DELETE FROM claims WHERE ID = " + str(ID)
        self.cur.execute(link_sql)
        self.connection.commit()

    def closeConnection(self):
        self.connection.commit()
