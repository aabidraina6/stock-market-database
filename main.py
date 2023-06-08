from sqlconnect import *
from user import *


def view_users():
    cur = sql_query("SELECT * FROM User")
    if cur: display_cursor_table("Users", cur)


def search_company_by_symbol():
    while (1):
        v = inputbox("View Company", "Enter company symbol")
        if v is None: break
        symbol = v
        cur = sql_query("SELECT * FROM Company WHERE Symbol LIKE %s", [symbol])
        if cur and cur.rowcount == 0:
            display("Error", "Invalid company symbol")
        else:
            display_cursor_table("Company Details", cur)
            break


def search_company_by_name():
    while (1):
        v = inputbox("View Company", "Enter company name")
        if v is None: break
        name = v
        cur = sql_query("SELECT * FROM Company WHERE Name LIKE %s", [name])
        if cur and cur.rowcount == 0:
            display("Error", "Invalid company name")
        else:
            display_cursor_table("Company Details", cur)
            break


def list_companies():
    cur = sql_query("SELECT * FROM Company")
    if cur: display_cursor_table("Companies", cur)


def landing_menu():
    """
    This is the landing menu for the user.
    This menu is displayed when the user logs in.
    """

    menu(
        "Menu",
        {
            # "View Stock": view_stock,
            # "View Portfolio": view_portfolio,
            # "View Transactions": view_transactions,
            "User Profile": {
                "Change Details": user_change_details,
                "Delete Account": user_delete_account,
                "Back": "Back",
            },
            "Search company": {
                "Search by name": search_company_by_name,
                "Search by symbol": search_company_by_symbol,
                "Back": "Back",
            },
            "List companies": list_companies,
            "Sign out and exit": exit,
            "Sign out": user_sign_out,
        },
        {"View Users": view_users} if user_isroot() else {})


if __name__ == "__main__":
    sql_try_connect()
    current_user["Name"] = "root"
    landing_menu()
    while 1:
        user_auth()
        if current_user["Name"]:
            landing_menu()