from ui import *
from sqlconnect import *

current_user = {
    "Name": None,
}


def user_isroot():
    return current_user["Name"] == "root"


def user_sign_out():
    current_user["Name"] = None


def user_sign_in():
    while (1):
        v = input_values("Sign in", {
            "username": "Enter username",
            "password": "Enter password",
        })
        if v is None: break
        username = v["username"]
        password = v["password"]
        cur = sql_query("SELECT * FROM User WHERE Name = %s AND Password = %s",
                        [username, password])

        if cur and cur.rowcount == 0:
            display("Error", "Invalid username or password\nPlease try again")
        else:
            current_user["Name"] = username
            break


def user_sign_up():
    while (1):
        v = inputbox("Sign up", "Enter username")
        if v is None: break
        username = v
        cur = sql_query("SELECT * FROM User WHERE Name = %s", [username])
        if (cur and cur.rowcount != 0):
            display("Error", "Username already exists, please try again")
            continue
        v = {}
        while (1):
            v = input_values("Enter details", {
                "password": "Enter password",
                "contact": "Enter contact",
                "email": "Enter email",
                "address": "Enter address",
                "location": "Enter location",
                "pan": "Enter PAN card number",
            },
                             default=v)
            if v is None: return
            cur = sql_query(
                """INSERT INTO User(`Name`,`Password`, `Contact`, `Email`, `Location`, `PAN_Info`)
                                VALUES(%s, %s,%s,%s,%s,%s)""", [
                    username,
                    v["password"],
                    v["contact"],
                    v["email"],
                    v["location"],
                    v["pan"],
                ],
                commit=True,
                success_msg="User created successfully",
                fail_msg="Failed to create user")
            if cur:
                return


def user_auth():
    menu("Stock Market Database", {
        "Sign in": user_sign_in,
        "Sign up": user_sign_up,
        "Exit": exit,
    })


def user_change_details():
    v = input_values(
        "Enter details", {
            "password": "Enter password",
            "contact": "Enter contact",
            "email": "Enter email",
            "location": "Enter location",
            "pan": "Enter PAN card number",
        })
    if v is None: return
    sql_query(
        "UPDATE User SET `Password`=%s, `Contact`=%s, `Email`=%s, `Location`=%s, `PAN_Info`=%s WHERE Name=%s",
        [
            v["password"],
            v["contact"],
            v["email"],
            v["location"],
            v["pan"],
            current_user["Name"],
        ],
        commit=True,
        success_msg="Details updated successfully",
        fail_msg="Failed to update details")


def user_delete_account():
    if confirm("Confirm delete",
               "Are you sure you want to delete your account? (y/n): "):
        sql_query("DELETE FROM User WHERE Name=%s", [current_user["Name"]],
                  commit=True,
                  success_msg="User deleted successfully",
                  fail_msg="Failed to delete user")
    else:
        display("Info", "Account not deleted")
