# Settings and credentials to allow access, read and modify data in
# Google Sheets
import gspread
from google.oauth2.service_account import Credentials

# time and sys libraries to add typing effect/delay
import time
import sys

# os library to clear screen
import os

# colorama for text formatting
# tutorial: https://linuxhint.com/colorama-python/
import colorama
from colorama import Fore, Back, Style

# initialize colorama
colorama.init(autoreset=True)

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


# clear screen function
# Credit: https://www.101computing.net/python-typing-text-effect/
def clearScreen():
    """
    Function for clearing CLI for new code
    """
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
    print("\n")
    print(Fore.CYAN + '''
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
    print("\n")
    print(Fore.CYAN + "             Sales & Inventory Management "
          "for Micro Bakeries.\n")
    time.sleep(1)
    print(Fore.CYAN + "      (Created for Educational Purposes -"
          " Copyright: Amy Richardson '23)")
    time.sleep(3)
    clearScreen()


def return_main():
    """
    Return to main menu
    """
    while True:
        print("\n")
        choice = typeInput("To return to Main Menu, please enter 'M'.\n")
        if choice == 'M' or choice == 'm':
            time.sleep(1.5)
            clearScreen()
            main()
            break
        else:
            print(Fore.RED + "Invalid input, please try again.")
            continue


def print_sales():
    """
    Print sales data by date to terminal
    """
    clearScreen()
    sales_sheet = SHEET.worksheet("sales").get_all_values()
    print(Back.MAGENTA + Fore.WHITE + "*** SALES FIGURES BY DATE ***\n")
    time.sleep(1)
    print(Fore.CYAN + """
                        - FLAVOURS LIST -
                        *****************
            Van  ->  Vanilla       Red V  ->  Red Velvet
            Choc ->  Chocolate     Strawb ->  Strawberry
            Cara ->  Caramel       C&C    ->  Cookies & Cream
          """)
    # \t to format and display sales data from gsheet into terminal
    # credit: https://tinyurl.com/3h7nr24a
    print("****************************************************************\n")
    for row in sales_sheet:
        print('\t'.join(row))
    print("\n")
    print("****************************************************************\n")
    print("\n")
    while True:
        choice = typeInput("To return to Sales Menu, please enter 'S'.\n")
        if choice == 'S' or choice == 's':
            time.sleep(1.5)
            clearScreen()
            day_sales()
            break
        else:
            print(Fore.RED + "Invalid input, please try again.")
            continue


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
        print(Fore.RED + "Input invalid, please try again.\n")
        sales_input()
        return False

    return True


def sales_input():
    """
    Allow user input of date and sales figures to be entered
    and used to update sales worksheet.
    """
    clearScreen()
    print(Back.MAGENTA + Fore.WHITE + "*** SALES INPUT ***\n")
    typePrint("Enter date & sales figures "
              "(DD,MM,YYYY, sales figures, separated by commas).\n")
    sales_figs = typeInput("Enter sales here: \n")
    sales_data = sales_figs.split(",")
    validate_sales(sales_data)
    sales_str = ','.join(sales_data)
    print(Fore.GREEN + f"You have entered : {sales_str}\n")
    while True:
        choice = typeInput("Please confirm: Y or N.\n")
        if choice == 'Y' or choice == 'y':
            sales_sheet = SHEET.worksheet("sales")
            sales_sheet.append_row(sales_data)
            typePrint("The sales figures have been recorded.\n")
            time.sleep(1)
            print("\n")
            day_sales()
            break
        elif choice == 'N' or choice == 'n':
            sales_input()
            break
        else:
            print(Fore.RED + "Invalid input, please try again.")
            continue


def clear_sales():
    """
    Clear all sales data from sales worksheet
    """
    clearScreen()
    print(Back.MAGENTA + Fore.WHITE + "*** CLEAR ALL SALES DATA ***\n")
    choice = typeInput("To clear all Sales Data please enter 'CLEAR DATA'.\n")
    if choice == 'CLEAR DATA':
        typePrint("Please confirm Y or N to clear all data:\n")
        final_c = typeInput("Enter choice here: \n")
        if final_c == 'Y' or final_c == 'y':
            sales_sheet = SHEET.worksheet("sales")
            # Clear a certain range
            # Credit: https://tinyurl.com/y3dfpe5v
            sales_sheet.batch_clear(["A2:J10000"])
            time.sleep(1)
            print(Fore.GREEN + "Sales sheet successfully cleared.")
            day_sales()
        elif final_c == 'N' or final_c == 'n':
            print(Fore.YELLOW + "Abort data delete.")
            day_sales()
        else:
            print(Fore.RED + "Invalid input. Returning to Sales menu.")
            time.sleep(1.5)
            day_sales()
    else:
        print(Fore.RED + "Invalid input.\n")
        check_c = typeInput("Please enter 'C' to continue or 'X' to exit.\n")
        if check_c == 'C' or check_c == 'c':
            clear_sales()
        elif check_c == 'X' or check_c == 'x':
            day_sales()
        else:
            print(Fore.RED + "Invalid input. Returning to main menu.")
            time.sleep(1.5)
            return_main()


def day_sales():
    """
    Go to sales menu
    """
    clearScreen()
    print(Back.MAGENTA + Fore.WHITE + "*** SALES MENU ***")
    while True:
        print(Fore.CYAN + """
            1. View sales data\n
            2. Add days sales\n
            3. Clear data\n
            4. Main menu
            """)
        try:
            choice = int(typeInput("Please choose from menu.\n"))
            if choice == 1:
                print_sales()
                break
            elif choice == 2:
                sales_input()
                break
            elif choice == 3:
                clear_sales()
                break
            elif choice == 4:
                return_main()
                break
        except ValueError:
            typePrint("Invalid input. Please choose a numbered menu item.")
            time.sleep(1.5)
            clearScreen()
            continue


def user_update_batch():
    """
    Allow user input to update next day batch levels
    """
    batch_sheet = SHEET.worksheet("batch")
    records = batch_sheet.get_all_records()
    while True:
        flav = input("Enter flavour as displayed above: \n")
        record_found = False
        for record in records:
            if record["Flavour"] == flav:
                record_found = True
                while True:
                    try:
                        update_q = int(input(f"Enter value for {flav}:\n"))
                        record["Quantity"] = update_q
                        # update with new data to inventory sheet
                        # credit: https://realpython.com/python-enumerate/
                        # credit: Tech with Tim->
                        # https://www.youtube.com/watch?v=-MZiQaNI0QA
                        for i, record in enumerate(records, start=2):
                            batch_sheet.update_cell(i, 2, record["Quantity"])
                        print(Fore.GREEN + "Inventory successfully updated.\n")
                        print(Back.MAGENTA + Fore.WHITE +
                              "** TODAYS BATCH NUMBERS **\n")
                        batch_sheet = SHEET.worksheet("batch")
                        batch_list = batch_sheet.col_values(1)
                        q_list = batch_sheet.col_values(2)
                        # list/zip for parallel iteration
                        # credit: https://realpython.com/python-zip-function/
                        # credit: Tech with Tim
                        # https://www.youtube.com/watch?v=-MZiQaNI0QA
                        pairs = list(zip(batch_list, q_list))
                        for pair in pairs:
                            print(Fore.CYAN + '- ', pair[0],
                                  Fore.CYAN + ': ', pair[1])
                        print("\n")
                        print(Fore.YELLOW + "ATTN: Batch = 12 cupcakes.\n")
                        choice = input("Update another flavour?"
                                       " Enter Y or N.\n")
                        if choice == 'Y' or choice == 'y':
                            user_update_batch()
                        elif choice == 'N' or choice == 'n':
                            return_main()
                    except ValueError:
                        print(Fore.RED + "Value must be numerical.\n")
                        continue
                    else:
                        return update_q
        if not record_found:
            print(Fore.RED + "Flavour not found in inventory.\n")
            continue


def check_batch():
    """
    Pull batch data from batch google sheet and allow
    user to update quantity and amend worksheet
    """
    typePrint("Fetching batch numbers for today...")
    time.sleep(1.5)
    clearScreen()
    print(Back.MAGENTA + Fore.WHITE + "** TODAYS BATCH NUMBERS **\n")
    batch_sheet = SHEET.worksheet("batch")
    batch_list = batch_sheet.col_values(1)
    q_list = batch_sheet.col_values(2)
    # list/zip for parallel iteration
    # credit: https://realpython.com/python-zip-function/
    # credit: Tech with Tim-https://www.youtube.com/watch?v=-MZiQaNI0QA
    pairs = list(zip(batch_list, q_list))
    for pair in pairs:
        print(Fore.CYAN + '- ', pair[0], Fore.CYAN + ': ', pair[1])
    print("\n")
    print(Fore.YELLOW + "ATTN: Batch = 12 cupcakes.\n")
    while True:
        user_input = input("Would you like to update batches? Enter Y or N.\n")
        if user_input == 'Y' or user_input == 'y':
            user_update_batch()
            break
        elif user_input == 'N' or user_input == 'n':
            return_main()
            break
    time.sleep(1)
    return_main()


def user_update_ing():
    """
    Allow user input to update inventory levels
    """
    invt_sheet = SHEET.worksheet("inventory")
    records = invt_sheet.get_all_records()
    while True:
        ing_c = input("Enter ingredient name as displayed above: \n")
        record_found = False
        for record in records:
            if record["Ingredient"] == ing_c:
                record_found = True
                while True:
                    try:
                        update_q = int(input(f"Enter value for {ing_c}:\n"))
                        record["Quantity"] = update_q
                        # update with new data to inventory sheet
                        # credit: https://realpython.com/python-enumerate/
                        for i, record in enumerate(records, start=2):
                            invt_sheet.update_cell(i, 2, record["Quantity"])
                        print(Fore.GREEN + "Inventory successfully updated.\n")
                        cho = input("Update another ingredient? Enter Y or N.")
                        print("\n")
                        if cho == 'Y' or cho == 'y':
                            user_update_ing()
                        elif cho == 'N' or cho == 'n':
                            return_main()
                        else:
                            print(Fore.RED + "Invalid input.\n")
                            check_invt()
                    except ValueError:
                        print(Fore.RED + "Value must be numerical.\n")
                        continue
        if not record_found:
            print(Fore.RED + "Ingredient not found in inventory.\n")
            continue


def check_invt():
    """
    Pull inventory data from inventory google sheet and allow
    user to update levels and amend worksheet
    """
    typePrint("Checking inventory levels...")
    time.sleep(1)
    clearScreen()
    print(Back.MAGENTA + Fore.WHITE + "*** CURRENT INVENTORY LEVELS ***\n")
    invt_sheet = SHEET.worksheet("inventory")
    ing_list = invt_sheet.col_values(1)
    q_list = invt_sheet.col_values(2)
    # list/zip for parallel iteration
    # credit: https://realpython.com/python-zip-function/
    pairs = list(zip(ing_list, q_list))
    for pair in pairs:
        print(Fore.CYAN + '- ', pair[0], Fore.CYAN + ': ', pair[1])
    print("\n")
    while True:
        try:
            u_input = input("Would you like to update an item? Enter Y or N\n")
            if u_input == 'Y' or u_input == 'y':
                user_update_ing()
                break
            elif u_input == 'N' or u_input == 'n':
                return_main()
                break
        except ValueError:
            print(Fore.RED + "Value must be numerical.\n")
            continue
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
    print(Back.MAGENTA + Fore.WHITE + "*** WELCOME TO BAKESTOCK ***\n")
    time.sleep(1)
    typePrint("Please choose from the menu below.\n")
    time.sleep(1)
    print("\n")
    print(Fore.CYAN + "1. Sales menu\n")
    print(Fore.CYAN + "2. Batch numbers\n")
    print(Fore.CYAN + "3. Ingredients inventory\n")
    print(Fore.CYAN + "4. Exit\n")
    while True:
        try:
            choice = int(typeInput("Please enter your choice: \n"))
            if choice == 1:
                day_sales()
                break
            elif choice == 2:
                check_batch()
                break
            elif choice == 3:
                check_invt()
                break
            elif choice == 4:
                exit()
                break
        except ValueError:
            print(Fore.RED + "Invalid input. Enter number for menu choice.\n")
            time.sleep(1)
            continue


prog_start()
main()
