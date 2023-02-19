# Settings and credentials to allow access, read and modify data in
# Google Sheets
import gspread
from google.oauth2.service_account import Credentials

# time and sys libraries to add typing effect/delay
import time,sys


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
    
    888888b.          88              .d888b.   88                  88
    888  "88b         88             d88P  Y88b 88                  88
    888  .8P          88             Y88b.      88                  88
    888888K.    888b. 88  88  .d88b.  "Y88b.    8888 .d88b.  .d888b 88  88
    888  "Y8b    "88b 88 .8P d8P  Y8b   "Y88b.  88   d8""8b d8P"    88 .8P
    888    88 .d88888 88888K 8888888"     "888  88   88  88 88      88888K
    888   d8P 888  88 88 "8b Y8b.    Y88b  d88P Y8b. Y8..8P Y8b.    88 "8b
    8888888P" "Y88888 88  88  "Y8888  "Y888P"   "Y88."Y88P"  "Y888P 88  88

    **********************************************************************
    ''')


def add_sales():
    """
    User adds sales data for days sales.
    """
    typePrint("Please enter days sales (7 numbers, separated by commas)... \n")
    data_str = typeInput("Enter sales here: \n")

    sales_data = data_str.split(",")
    
    typePrint(f"You have entered : {sales_data}\n")
    typeInput("Please confirm: Y or N\n")




def check_batch():
    """
    Pull next day batch nums from google sheets-batch
    """
    typePrint("Please enter date in format DD-MM-YYYY...")
    data_str = typeInput("Enter date here: \n")
    print('data_str')
    

def check_invt():
    """
    Pull inventory data from google sheet-inventory
    """
    typePrint("Checking inventory levels...\n")
    time.sleep(1)
    typePrint("Current inventory levels are: \n")


def main():
    """
    Menu is displayed with options for user input
    """
    typePrint("Welcome to BakeStock.\n")
    time.sleep(1) 
    print("\n")
    typePrint("Please choose from the menu below.\n")
    time.sleep(1)
    print("\n")
    print("1. Add daily sales.\n")
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
    
    choice = int(typeInput("Enter your choice: \n"))
    if choice == 1:
        add_sales()
    elif choice == 2:
        check_batch()
    elif choice == 3:
        check_invt()


prog_start()
main()


