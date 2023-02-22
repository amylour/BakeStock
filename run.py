# Settings and credentials to allow access, read and modify data in
# Google Sheets
import gspread
from google.oauth2.service_account import Credentials

# time and sys libraries to add typing effect/delay
import time
import sys

# os library to clear screen
import os


from datetime import datetime


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


# Dictionary of inventory ingredients and levels
ingInvt = {
    "Flour": "10000g",
    "Sugar": "12500g",
    "Butter": "7500g",
    "Eggs": "140",
    "Milk": "7800ml",
    "Cream Cheese": "4000g",
    "Icing Sugar": "22500g",
    "Chocolate": "2500g",
    "Cookies": "2000g",
    "Cocoa Powder": "2500g",
    "Vanilla Extract": "700ml",
    "Unsalted Butter": "11500g",
    "Strawberry Syrup": "300ml",
    "Caramel Syrup": "300ml"
}


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


def return_main():
    """
    Return to main menu
    """
    while True:
        choice = input("""
                       \n
                       \n
                       To return to Main Menu, please enter 'M'.
                       \n
                       """)
        if choice == 'M' or choice == 'm':
            time.sleep(1.5)
            clearScreen()
            main()
            break
        else:
            print("Invalid input, please try again.")
            continue


def print_sales():
    """
    Print sales data by date to terminal
    """
    sales_sheet = SHEET.worksheet("sales").get_all_values()
    # credit: https://stackoverflow.com/questions/4488570/how-do-i-write-a-tab-in-python
    print("****************************************************************\n")
    for row in sales_sheet:
        print('\t'.join(row))
    print("\n")
    print("****************************************************************\n")  
    time.sleep(2)
    return_main()

    
'''
def check_sales():
    """
    Check sales by date and print in terminal
    """
    clearScreen()
    typePrint("Please enter date in the format DD-MM-YYYY.\n")
    sales_date_str = typeInput("Enter date here: \n")
    if len(sales_date_str) == 10:
        try:
            typePrint(f"You have entered: {sales_date_str}\n")
while True:
    choice = typeInput("Please confirm: Y or N.\n")
    try:
        if choice == 'Y' or choice == 'y':
            sales_sheet = SHEET.worksheet("sales").get_all_values()
            # credit: https://stackoverflow.com/questions/4488570/how-do-i-write-a-tab-in-python
            for row in sales_sheet:
                print('\t'.join(row))                    
            break
        elif choice == 'N' or choice == 'n':
            check_sales()
            break
        else:
            print("Invalid input, please try again.")
            continue
    except ValueError:
        typePrint("Invalid input. Please enter date in format DD-MM-YYYY.")
        clearScreen()
        time.sleep(.5)
        check_sales()
        #except ValueError:
                #print("Invalid Date")
               # clearScreen()
                #time.sleep(.5)
                #check_sales()
    #else:
        #print("Invalid date format, please try again.")
        #time.sleep(2)
        #check_sales()
'''


def validate_sales(values):
    """
    Convert string values into integers and raise ValueError if 
    strings cannot be converted into int. Check for 6 values.
    Credit: Code Institute Love Sandwiches project
    """
    try:
        [int(value) for value in values]
        if len(values) != 9:
            raise ValueError(
                f"6 values required, you provided {len(values)}"
            )
    except ValueError:
        typePrint(f"Input invalid, please try again.\n")
        sales_input()
        return False

    return True

def sales_input():
    typePrint("Enter date & sales figures "
              "(DD,MM,YY, sales figures, separated by commas).\n")
    sales_figs = typeInput("Enter sales here: \n")
    sales_data = sales_figs.split(",")
    validate_sales(sales_data)
    sales_str = ','.join(sales_data)
    typePrint(f"You have entered : {sales_str}\n")
    while True:
        choice = typeInput("Please confirm: Y or N.\n")
        if choice == 'Y' or choice == 'y':
            sales_sheet = SHEET.worksheet("sales")
            sales_sheet.append_row(sales_data)
            typePrint(f"The sales figures have been recorded.\n")
            time.sleep(1)
            print("\n")
            return_main()
            break
        elif choice == 'N' or choice == 'n':
            sales_input()
            break
        else:
            print("Invalid input, please try again.")
            continue
    
'''
def rec_sales():
    """
    Record daily sales
    """
    # typePrint("Please enter date in the format DD-MM-YYYY.\n")
    # rec_date = typeInput("Enter date here: \n")
    #gs_date_rec = datetime.strftime(rec_date, '%d/%m/%Y')
    # if len(rec_date) == 10:
         #try:
    # typePrint(f"You have entered: {rec_date}\n")
    typePrint("Getting todays date...\n")
    time.sleep(1)
    now = datetime.now()
    date_str = now.strftime("%d-%m-%Y")
    print(f"Todays date is {date_str}\n")
    while True:
        choice = typeInput("Please confirm: Y or N.\n")
        try:
            if choice == 'Y' or choice == 'y':
                sales_input()
                break
            elif choice == 'N' or choice == 'n':
                rec_sales()
                break
            else:
                print("Invalid input, please try again.")
                continue
        except ValueError:
            typePrint("Invalid input. Enter date in format DD-MM-YYYY.")
            clearScreen()
            time.sleep(.5)
            rec_sales()
       # except ValueError:
               # print("Invalid Date.")
               # clearScreen()
               # time.sleep(.5)
               # rec_sales()
    #else:
        #print("Invalid date format, please try again.")
        #time.sleep(2)
        #rec_sales()
'''

    
def day_sales():
    """
    Go to sales menu
    """
    clearScreen()
    print("** Sales Menu **")
    while True:
        print("""
            1. View sales data.
            2. Add days sales.
            """)
        try:
            choice = int(typeInput("Please choose from menu.\n"))
            if choice == 1:
                print_sales()
                break
            elif choice == 2:
                sales_input()
                break
        except ValueError:
            typePrint("Invalid input. Please choose a numbered menu item.")
            time.sleep(1.5)
            clearScreen()
            continue

def print_batch():
    """
    Print batch numbers from date input
    """
    print("You have reached print batch.")
    time.sleep(1)
    return_main()


def check_batch():
    """
    Pull date of day batch nums data from google sheets-batch
    """
    clearScreen()
    time.sleep(0.5)
    typePrint("Please enter date in format DD-MM-YYYY.\n")
    data_str = typeInput("Enter date here: \n")
    if len(data_str) == 10:
        try:
            typePrint(f"You have entered: {data_str}\n")
            while True:
                choice = typeInput("Please confirm: Y or N\n")
                try:
                    if choice == 'Y' or choice == 'y':
                        print_batch()
                        break
                    elif choice == 'N' or choice == 'n':
                        check_batch()
                        break
                    else:
                        print("Invalid input, please try again")
                        continue
                except ValueError:
                    typePrint("Invalid input. Please enter date in format DD-MM-YYYY.")
                    clearScreen()
                    time.sleep(.5)
                    check_batch()
        except ValueError:
                print("Invalid Date")
                clearScreen()
                time.sleep(.5)
                check_batch()
    else:
        print("Invalid date format, please try again.")
        time.sleep(2)
        check_batch()


def check_invt():
    """
    Pull inventory data from google sheet-inventory
    Print list vertically credit: thispointer.com https://tinyurl.com/r5ctr7je
    """
    typePrint("Checking inventory levels...")
    time.sleep(1)
    clearScreen()
    typePrint(f"Current inventory levels are:\n")
    for key, value in ingInvt.items():
        print('- ', key, ':', value)
    print("\n")
    while True:
        user_input = input("Would you like to update an item? Enter Y or N.\n")
        if user_input == 'Y' or user_input == 'y':
            clearScreen()
            update_invt()
            break
        elif user_input == 'N' or user_input == 'n':
            return_main()  
            break 
    time.sleep(1)
    return_main()


def user_update():
    while True:
        ing_name = input("Please choose ingredient from the list: \n")
        if ing_name in ingInvt:
            updated_value = input("Enter new value for ingredient: \n")
            ingInvt[ing_name] = updated_value
            print(f"{ing_name} updated to {updated_value}\n")
            break
        else:
            print(f"{ing_name} is not in this list.\n")
            continue
    

def update_invt():
    """
    Allow user to add additional ingredient amounts to increase
    inventory levels.
    """
    clearScreen()
    typePrint("Update inventory levels.")
    print("\n")
    typePrint("Current Inventory levels are: ")
    print("\n")
    time.sleep(1)
    for key, value in ingInvt.items():
        print('- ', key, ':', value)
    user_update()
    clearScreen()
    typePrint("Updated inventory levels are: \n")
    for key, value in ingInvt.items():
        print('- ', key, ':', value)
    time.sleep(1)
    return_main()


def calc_pro():
    """
    Calculate daily profits by subtracting total batch cost from
    daily sales figure. Append profit worksheet to include days profits.
    """
    typePrint("Please enter date in format DD-MM-YYYY.\n")
    data_str = typeInput("Enter date here: \n")
    time.sleep(1)
    return_main()



def exit():
    """
    return to program start screen
    """
    typePrint("Returning to program start...")
    time.sleep(2)
    print("\n")
    print("\n")
    clearScreen()

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
    print("2. Check batch numbers.\n")
    print("3. Check ingredients inventory.\n")
    print("4. Update ingredients inventory.\n")
    print("5. Calculate profits.\n")
    print("6. Exit.")
    print('''
      *******************************************************
      * ALERT: Inventory levels normal.                     *
      *******************************************************
      ''')
    while True:
        try:
            choice = int(typeInput("Please enter your choice: \n"))
            if choice == 1:
                day_sales()
                break
            elif choice == 2:
                check_batch()#
                break
            elif choice == 3:
                check_invt()
                break
            elif choice == 4:
                update_invt()
                break
            elif choice == 5:
                calc_pro()
                break
            elif choice == 6:
                exit()
                break
        except ValueError:
            typePrint("Invalid input. Please choose a numbered menu item...\n")
            time.sleep(1)
            continue
            
            


prog_start()
main()
