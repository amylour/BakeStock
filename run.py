# Settings and credentials to allow access, read and modify data in
# Google Sheets
import gspread
from google.oauth2.service_account import Credentials

# time and sys libraries to add typing effect/delay
import time
import sys

# os library to clear screen
import os

# Scope for Google IAM auth for API program access
SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]


# const for untracked creds file
CREDS = Credentials.from_service_account_file('creds.json')
# const for credentials scope
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
# const to allow auth of gspread client within these scoped credentials
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
# const for google sgeet
SHEET = GSPREAD_CLIENT.open('bakestock')

# clear screen function Credit: https://www.101computing.net/python-typing-text-effect/
def clearScreen():
    os.system("clear")


# typing effect function with delay effect for print and input
# print() replaced with typePrint() and input() replaced with typeInput()
# time.sleep() used as a pause effect with seconds parameter
# credit: https://www.101computing.net/python-typing-text-effect/
def typePrint(text):
    for character in text:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)


def typeInput(text):
    for character in text:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    value = input()
    return value


def prog_start():
    """
    Run opening screen for user and display menu options for user
    """
    print('''
    **********************************************************************
    *                                                                    *
    888888b.          88              .d888b.   88                  88
    888  "88b         88             d88P  Y88b 88                  88
    888  .8P          88             Y88b.      88                  88
    888888K.    888b. 88  88  .d88b.  "Y88b.    8888 .d88b.  .d888b 88  88
    888  "Y8b    "88b 88 .8P d8P  Y8b   "Y88b.  88   d8""8b d8P"    88 .8P
    888    88 .d88888 88888K 8888888"     "888  88   88  88 88      88888K
    888   d8P 888  88 88 "8b Y8b.    Y88b  d88P Y8b. Y8..8P Y8b.    88 "8b
    8888888P" "Y88888 88  88  "Y8888  "Y888P"   "Y88."Y88P"  "Y888P 88  88
    *                                                                    *
    **********************************************************************
    ''')


def check_sales():
    """
    Check sales by date and print in terminal
    """
    clearScreen()
    typePrint("Please enter date in the format DD-MM-YYYY... \n")
    data_str = typeInput("Enter date here: \n")

    date_data = data_str.split(" " + "-" + " " + "-" + " ")
    typePrint(f"You have entered : {date_data}\n")
    typeInput("Please confirm: Y or N\n")


def rec_sales():
    """
    Record daily sales
    """
    typePrint("Please enter days sales (6 numbers, separated by commas)... \n")
    data_str = typeInput("Enter sales here: \n")

    sales_data = data_str.split(",")
    typePrint(f"You have entered : {sales_data}\n")
    typeInput("Please confirm: Y or N\n")


def day_sales():
    """
    Go to sales menu
    """
    clearScreen()
    typePrint("Sales Menu")
    time.sleep(1)
    print("""
          1. Check sales by date
          2. Add days sales
          """)
    try:
        choice = int(typeInput("Please choose from menu...\n"))
        if choice == 1:
            check_sales()
        elif choice ==2:
            rec_sales()
    except ValueError:
        typePrint("Invalid input. Please choose a numbered menu item...")
        time.sleep(1.5)
        clearScreen()
        day_sales()


def check_batch():
    """
    Pull next day batch nums from google sheets-batch
    """
    typePrint("Please enter date in format DD-MM-YYYY...\n")
    data_str = typeInput("Enter date here: \n")
    print('data_str')


def check_invt():
    """
    Pull inventory data from google sheet-inventory
    """
    typePrint("Checking inventory levels...")
    time.sleep(1)
    print("\n")
    typePrint("Current inventory levels are: ")
    print("\n")


def update_invt():
    """
    Allow user to add additional ingredient amounts to increase
    inventory levels.
    """
    typePrint("Please choose ingredient from the list: \n")
    time.sleep(1)
    print("""
          1.  Flour
          2.  Sugar
          3.  Butter
          4.  Eggs
          5.  Milk
          6.  Cream Cheese
          7.  Icing Sugar
          8.  Chocolate
          9.  Cookies
          10. Cocoa Powder
          11. Vanilla Extract
          12. Unsalted Butter
          13. Strawberry Syrup
          14. Caramel Syrup 
          """)

    choice = int(typeInput("Enter your choice: \n"))


def calc_pro():
    """
    Calculate daily profits by subtracting total batch cost from
    daily sales figure. Append profit worksheet to include days profits.
    """
    typePrint("Please enter date in format DD-MM-YYYY...\n")
    data_str = typeInput("Enter date here: \n")


def exit():
    """
    return to program start screen
    """
    typePrint("Returning to program start...")
    time.sleep(2)
    print("\n")
    print("\n")

    prog_start()
    main()
 

def main():
    """
    Menu is displayed with options for user input
    """
    typePrint("Welcome to BakeStock.\n")
    time.sleep(1)
    typePrint("Please choose from the menu below.\n")
    time.sleep(1)
    print("\n")
    print("1. Sales menu.\n")
    print("2. Check next day batch numbers.\n")
    print("3. Check ingredients inventory.\n")
    print("4. Update ingredients inventory.\n")
    print("5. Calculate profits.\n")
    print("6. Exit.\n")

    print('''
      *******************************************************
      * ALERT: Inventory levels normal.                     *
      *******************************************************
      ''')
    try:
        choice = int(typeInput("Enter your choice: \n"))
        if choice == 1:
            day_sales()
        elif choice == 2:
            check_batch()
        elif choice == 3:
            check_invt()
        elif choice == 4:
            update_invt()
        elif choice == 5:
            calc_pro()
        elif choice == 6:
            exit()
    except ValueError:
        typePrint("Invalid input. Please choose a numbered menu item...")
        time.sleep(1.5)
        clearScreen()
        main()


prog_start()
main()
