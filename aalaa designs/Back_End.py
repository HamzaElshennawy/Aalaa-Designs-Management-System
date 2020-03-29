import sqlite3
from tkinter import *
#this is the main database 
def aalaa_designs_data():
    connect=sqlite3.connect("AD.db")
    cur=connect.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS AD(id INTEGER PRIMARY KEY, Name text, Date text, \
    cde text, Address text, Mobile text, wight text, length text ,orderr text,history text)")
    connect.commit()
    connect.close()
    
#this is the add data button 
def add_pt_data( Name, Date, cde, Address, Mobile,wight,length,orderr,history):
    connect=sqlite3.connect("AD.db")
    cur=connect.cursor()
    cur.execute("INSERT INTO AD VALUES (NULL,?,?,?,?,?,?,?,?,?)",(Name, Date, cde, Address, Mobile,wight,length,orderr,history))
    connect.commit()
    connect.close()

#this is the view data button
def viewptdata():
    connect=sqlite3.connect("AD.db")
    cur=connect.cursor()
    cur.execute("SELECT * FROM AD")
    rows=cur.fetchall()
    connect.close()
    return rows

#this is the delete record
def deletedata(id):
    connect=sqlite3.connect("AD.db")
    cur=connect.cursor()
    cur.execute("DELETE FROM AD WHERE id=?",(id,))
    connect.commit()
    connect.close()    


def searchdata(Name="" , Date="" , cde="", Address="", Mobile="",wight="",length="",orderr="",history=""):
    connect=sqlite3.connect("AD.db")
    cur=connect.cursor()
    cur.execute("SELECT * FROM AD WHERE Name=? OR Date=? OR cde=? OR Address=? OR Mobile=? OR wight=? OR length=? OR orderr=? OR history=?" , \
                (Name , Date , cde , Address , Mobile , wight, length, orderr,history))
    rows=cur.fetchall()
    connect.close() 
    return rows


def updatedata(Name="", cde="",Date="",  Address="", Mobile="",wight="",length="",orderr="",history=""):
    connect=sqlite3.connect("AD.db")
    cur=connect.cursor()
    cur.execute("INSERT INTO AD VALUES (NULL,?,?,?,?,?,?,?,?,?)",(Name,cde,Date,Address,Mobile,wight,length,orderr,history))
    connect.commit()
    connect.close() 



aalaa_designs_data()
