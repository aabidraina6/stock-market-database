import pymysql.cursors
from ui import *

con = None
cur = None


def sql_try_connect():
    global con, cur
    try:
        # Set db name accordingly which have been create by you
        # Set host to the server's address if you don't want to use local SQL server
        con = pymysql.connect(
            host='localhost',
            user="root",
            password="root",
            db="stock_db",
            # cursorclass=pymysql.cursors.DictCursor,
        )
        #   unix_socket="/var/run/mysqld/mysqld.sock")
        if (con.open):
            print("Connected to SQL server")
            cur = con.cursor()
        else:
            print("Failed to connect to SQL server")
            exit()
    except Exception as e:
        print(e)
        print("Failed to connect to SQL server")
        exit()


def sql_query(query, args=[], commit=False, success_msg="", fail_msg=""):
    try:
        cur.execute(query, args)
        if commit:
            con.commit()
        if success_msg:
            display("Info", success_msg)
        return cur
    except Exception as e:
        con.rollback()
        display("Database Error", fail_msg + "\nError: {}".format(e))
        return None