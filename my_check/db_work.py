#!/usr/bin/python
# -*- coding: utf-8 -*-
 
import psycopg2
import sys
 
 
con = None
db = "host='localhost' dbname='checkdb' user='vova_virtualbox' password='qwerty1111'"

def select():
    try:
        con = psycopg2.connect(db)   
        cur = con.cursor()
        cur.execute("SELECT * FROM my_app_check")
     
        while True:
            row = cur.fetchone()
     
            if row == None:
                break
     
            print("Name: " + row[1] + "\t\tAge: " + str(row[2]))
     
    except psycopg2.DatabaseError, e:
        if con:
            con.rollback()
     
        print 'Error %s' % e    
        sys.exit(1)
     
    finally:   
        if con:
            con.close()


def update():
    try:
        con = psycopg2.connect(db)   
        cur = con.cursor()
        cur.execute("INSERT INTO my_app_check VALUES(4, 'Anton', 23)")      
        con.commit()
    except psycopg2.DatabaseError, e:
        if con:
            con.rollback()
 
        print 'Error %s' % e    
        sys.exit(1)
     
    finally:   
        if con:
            con.close()
