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
    Run opening screen for user and gives brief explanation of its use.
    """
    print("\n")
    # Fore and Style options are colorama properties to give the text colours
    print(Fore.CYAN + Style.BRIGHT + '''
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
    print(Fore.CYAN + Style.BRIGHT + "           Sales & Inventory Management "
          "for Hobby Bakers.\n")
    time.sleep(1)
    print(Fore.CYAN + Style.BRIGHT + "     (Created for Educational Purposes -"
          " Copyright: Amy Richardson '23)")
    time.sleep(3)
    clearScreen()


def return_main():
    """
    Return to main menu option through user input.
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
            # Invaid input displayed in red for attention
            print(Fore.RED + "Invalid input, please try again.")
            continue


def print_sales():
    """
    Print sales data to terminal for user to view.
    """
    clearScreen()
    # Pulls Sales data from Google Sheets
    sales_sheet = SHEET.worksheet("sales").get_all_values()
    print(Back.MAGENTA + Fore.WHITE + Style.BRIGHT +
          "*** SALES FIGURES BY DATE ***\n")
    # \t to format and display sales data from gsheet into terminal
    # credit: https://tinyurl.com/3h7nr24a
    print("****************************************************************\n")
    print("-Day- -Month-  -Year-                -Baked Items-\n")
    for row in sales_sheet:
        print('\t'.join(row))
    print("\n")
    print("****************************************************************\n")
    print("\n")
    # Displays warning to user if no Sales available in Google worksheet
    # Important so that user is not surprised by a blank data table
    if len(sales_sheet) == 0:
        print(Fore.YELLOW + Style.BRIGHT + "No Sales Data available.\n")
    while True:
        choice = typeInput("To return to Sales Menu, please enter 'S'.\n")
        if choice == 'S' or choice == 's':
            time.sleep(1.5)
            clearScreen()
            day_sales()
            break
        else:
            print(Fore.RED + "Invalid input, please try again.")
            time.sleep(1)
            continue


def validate_sales(values):
    """
    Convert string values into integers and raise ValueError if
    strings cannot be converted into int. Check for 6 values.
    Credit: Code Institute Love Sandwiches project.
    """
    try:
        [int(value) for value in values]
        if len(values) != 9:
            raise ValueError(
                f"6 values required, you provided {len(values)}"
            )
    except ValueError:
        print(Fore.RED + "Input invalid, please try again.\n")
        time.sleep(1)
        sales_input()
        return False

    return True


def sales_input():
    """
    Allow user input of date, bakes items and sales figures to be entered
    and used to update Sales worksheet.
    """
    clearScreen()
    print(Back.MAGENTA + Fore.WHITE + Style.BRIGHT +
          "*** SALES INPUT ***\n")
    # Clear instructions for user to follow on how to input the data
    print(Fore.CYAN + "Enter Date & abbreviated Baked items (max 4 letters):")
    typePrint("(DD,MM,YYYY, six Baked items, separated by commas).\n")
    sales_figs = input(Fore.YELLOW + Style.BRIGHT + "Enter here: \n")
    sales_data = sales_figs.split(",")
    sales_sheet = SHEET.worksheet("sales")
    # Ensure the correct amount of data is provided for Sales table
    # to be displayed correctly.
    if len(sales_data) > 9:
        print(Fore.RED + "Too many values. Please re-enter Date & Items.\n")
        time.sleep(2)
        sales_input()
    sales_str = ','.join(sales_data)
    print(Fore.CYAN + Style.BRIGHT + "Enter Date & Sales numbers:")
    typePrint("(DD,MM,YYYY, six Sales numbers, separated by commas).\n")
    sales_nums = input(Fore.YELLOW + Style.BRIGHT + "Enter here: \n")
    sales_num_data = sales_nums.split(",")
    validate_sales(sales_num_data)
    sales_num_str = ','.join(sales_num_data)
    print(Fore.GREEN + Style.BRIGHT + f"You have entered : {sales_str}\n")
    print(Fore.GREEN + Style.BRIGHT + f"You have entered : {sales_num_str}\n")
    # Asks user to confirm their entered data to ensure accuracy
    while True:
        choice = typeInput("Please confirm: Y or N.\n")
        if choice == 'Y' or choice == 'y':
            sales_sheet = SHEET.worksheet("sales")
            sales_sheet.append_row(sales_data)
            sales_sheet.append_row(sales_num_data)
            # Successful update text in green for attention
            print(Fore.GREEN + "The Sales figures have been recorded.\n")
            typePrint(" Returning to Sales Menu...\n")
            time.sleep(1.5)
            print("\n")
            day_sales()
            break
        elif choice == 'N' or choice == 'n':
            sales_input()
            break
        else:
            print(Fore.RED + "Invalid input, please try again.")
            time.sleep(1.5)
            continue


def clear_sales():
    """
    Clear all Sales data from sales worksheet
    User must follow the instructions exactly
    to ensure no accidental deleting.
    """
    clearScreen()
    print(Back.MAGENTA + Fore.WHITE + Style.BRIGHT +
          "*** CLEAR ALL SALES DATA ***\n")
    choice = typeInput("To clear all Sales data please enter 'CLEAR DATA'.\n")
    if choice == 'CLEAR DATA':
        typePrint("Please confirm Y or N to clear all data:\n")
        final_c = typeInput("Enter choice here: \n")
        if final_c == 'Y' or final_c == 'y':
            sales_sheet = SHEET.worksheet("sales")
            # Clear a certain range
            # Credit: https://tinyurl.com/y3dfpe5v
            sales_sheet.clear()
            time.sleep(1)
            print(Fore.GREEN + "Sales sheet successfully cleared.")
            day_sales()
        elif final_c == 'N' or final_c == 'n':
            print(Fore.YELLOW + Style.BRIGHT + "Abort data delete.")
            day_sales()
        else:
            # Failsafe to return to Main Menu incase of accidental key entry
            print(Fore.RED + "Invalid input. Returning to Sales menu.")
            time.sleep(1.5)
            day_sales()
    else:
        print(Fore.RED + "Invalid input.\n")
        # Failsafe to ask user to confirm choice incase of accidental key entry
        check_c = typeInput("Please enter 'C' to continue or 'X' to exit.\n")
        if check_c == 'C' or check_c == 'c':
            clear_sales()
        elif check_c == 'X' or check_c == 'x':
            day_sales()
        else:
            print(Fore.RED + "Invalid input. Returning to Main Menu.")
            time.sleep(1.5)
            clearScreen()
            main()


def day_sales():
    """
    Go to Sales menu and display Menu options for user
    Input is validated to ensure correct choice
    """
    clearScreen()
    print(Back.MAGENTA + Fore.WHITE + Style.BRIGHT + "*** SALES MENU ***")
    while True:
        print(Fore.CYAN + Style.BRIGHT + """
            1. View Sales Data\n
            2. Add Days Sales\n
            3. Clear Data\n
            4. Main Menu
            """)
        try:
            choice = int(typeInput("Please choose from Menu.\n"))
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
                clearScreen()
                main()
                break
        except ValueError:
            print(Fore.RED +
                  "Invalid input. Please choose a numbered menu item.")
            time.sleep(1.5)
            day_sales()
            continue


def return_batch_menu():
    """
    Print updated Batch number data for user from google Sheet and
    provide input choices for uer to update Batches
    """
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
    # Alert to remind users that a batch is 12 baked Items
    # Displayed in yellow for attention
    print(Fore.YELLOW + Style.BRIGHT + "ATTN: Batch = 12 baked items.\n")
    while True:
        user_input = input("Would you like to update Batches? Enter Y or N.\n")
        if user_input == 'Y' or user_input == 'y':
            print("\n")
            batch_options()
            break
        elif user_input == 'N' or user_input == 'n':
            return_main()
            break


def add_batch_item():
    """
    Add new batch item and quantity and update Google Sheet.
    """
    batch_sheet = SHEET.worksheet("batch")
    new_batch = input("Enter a new Batch item to record (eg: Mint Choc): \n")
    while True:
        try:
            new_batch_q = int(input("Enter new Batch quantity"
                                    " (numerical value only): \n"))
            break
        except ValueError:
            print(Fore.RED + "Invalid input, numerical value needed.\n")
    rows_used = len(batch_sheet.col_values(1))
    # Check to see if amount of rows used in the batch Google worksheet
    # is less than 7 so that only 6 Flavour/Baked items are accepted
    # User is informed in yellow if Batch records are full
    if rows_used < 7:
        batch_sheet.append_row([new_batch, new_batch_q])
        print(Fore.GREEN + "Batch records successfully updated.\n")
        return_batch_menu()
    else:
        print(Fore.YELLOW + Style.BRIGHT + "Sorry, Batch records full."
              " Max 6 Batch item types.\n")
        time.sleep(2)
        return_batch_menu()


def change_batch_item():
    """
    Change item name in Batch record and update Google Sheet.
    """
    batch_sheet = SHEET.worksheet("batch")
    col_vals = batch_sheet.col_values(1)
    batch_o = input("Enter Batch name as displayed above: \n")
    if batch_o in col_vals:
        # Find the correct cell using user input
        # User is informed if the input is not present in current records
        cell = batch_sheet.find(batch_o)
        batch_n = input("Enter the new batch item: \n")
        batch_sheet.update_cell(cell.row, cell.col, batch_n)
        print(Fore.GREEN + "Batch records successfully updated.\n")
        return_batch_menu()
    else:
        print(Fore.RED + "Item not found in Batches.\n")
        change_batch_item()


def clear_batch_item():
    """
    Clear Batch item completely from records, update Google worksheet.
    """
    batch_sheet = SHEET.worksheet("batch")
    col_vals = batch_sheet.col_values(1)
    batch_del = input("Enter Batch name as displayed above: \n")
    if batch_del in col_vals:
        # Find the correct cell using user input
        # User is informed if the input is not present in current records
        cell = batch_sheet.find(batch_del)
        batch_sheet.delete_rows(cell.row)
        print(Fore.GREEN + "Records updated successfully.\n")
        return_batch_menu()
    else:
        print(Fore.RED + "Item not found in Batches.\n")
        clear_batch_item()


def user_update_batch():
    """
    Allow user input to update next day Batch levels or
    update Batches as bakes have been completed.
    """
    batch_sheet = SHEET.worksheet("batch")
    records = batch_sheet.get_all_records()
    while True:
        flav = input("Enter Flavour/Item as displayed above: \n")
        record_found = False
        for record in records:
            if record["Flavour/Item"] == flav:
                record_found = True
                while True:
                    try:
                        update_q = int(input(f"Enter value for {flav}:\n"))
                        record["Quantity"] = update_q
                        # update with new data to Batch worksheet
                        # credit: https://realpython.com/python-enumerate/
                        # credit: Tech with Tim->
                        # https://www.youtube.com/watch?v=-MZiQaNI0QA
                        for i, record in enumerate(records, start=2):
                            batch_sheet.update_cell(i, 2, record["Quantity"])
                        print(Fore.GREEN + "Batches successfully updated.\n")
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
                        print(Fore.YELLOW + Style.BRIGHT +
                              "ATTN: Batch = 12 baked items.\n")
                        choice = input("Update another Flavour/Item?"
                                       " Enter Y or N.\n")
                        if choice == 'Y' or choice == 'y':
                            return_batch_menu()
                        elif choice == 'N' or choice == 'n':
                            return_main()
                    except ValueError:
                        print(Fore.RED + "Value must be numerical.\n")
                        continue
                    else:
                        return update_q
        if not record_found:
            print(Fore.RED + "Flavour/Item not found in Batches.\n")
            continue


def batch_options():
    """
    Menu to choose between adding new Batch item, changing Batch name
    or updating quantity.
    """
    print(Back.MAGENTA + Fore.WHITE + Style.BRIGHT + "*** BATCH MENU ***")
    print("\n")
    print(Fore.CYAN + Style.BRIGHT + "1. Add New Batch Item\n")
    print(Fore.CYAN + Style.BRIGHT + "2. Change Batch Item Name\n")
    print(Fore.CYAN + Style.BRIGHT + "3. Update Batch Number\n")
    print(Fore.CYAN + Style.BRIGHT + "4. Clear Batch Item\n")
    print(Fore.CYAN + Style.BRIGHT + "5. Return to Main Menu\n")
    while True:
        try:
            choice = int(input("Please choose from the Menu: \n"))
            if choice == 1:
                add_batch_item()
                break
            elif choice == 2:
                change_batch_item()
                break
            elif choice == 3:
                user_update_batch()
                break
            elif choice == 4:
                clear_batch_item()
                break
            elif choice == 5:
                clearScreen()
                main()
                break
        except ValueError:
            print(Fore.RED + "Invalid input. Enter number for Menu choice.\n")
            time.sleep(1)
            continue


def check_batch():
    """
    Pull Batch data from batch Google Sheet and allow
    user to update quantity and amend worksheet
    """
    typePrint("Fetching Batch numbers for today...")
    time.sleep(1.5)
    clearScreen()
    print(Back.MAGENTA + Fore.WHITE + Style.BRIGHT +
          "** TODAYS BATCH NUMBERS **\n")
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
    print(Fore.YELLOW + Style.BRIGHT + "ATTN: Batch = 12 baked items.\n")
    while True:
        user_input = input("Would you like to update Batches? Enter Y or N.\n")
        if user_input == 'Y' or user_input == 'y':
            print("\n")
            batch_options()
            break
        elif user_input == 'N' or user_input == 'n':
            return_main()
            break
    time.sleep(1)
    return_main()


def return_invt_menu():
    """
    Print updated Inventory data from Google worksheet for user and
    provide input choices to return to main Inventory menu.
    """
    invt_sheet = SHEET.worksheet("inventory")
    invt_list = invt_sheet.col_values(1)
    ing_list = invt_sheet.col_values(2)
    pairs = list(zip(invt_list, ing_list))
    for pair in pairs:
        print(Fore.CYAN + '- ', pair[0], Fore.CYAN + ': ', pair[1])
    print("\n")
    while True:
        user_input = input("Update Inventory? Enter Y or N.\n")
        if user_input == 'Y' or user_input == 'y':
            print("\n")
            invt_options()
            break
        elif user_input == 'N' or user_input == 'n':
            return_main()
            break


def add_ingredient():
    """
    Add new Ingredient by user input to Inventory
    and update Google Sheet.
    """
    invt_sheet = SHEET.worksheet("inventory")
    # Instructions for user to include item weight unit for accurate records
    new_ing = input("Enter a new Ingredient to add to the"
                    " Inventory (include unit eg: Cocoa Powder(g)): \n")
    while True:
        try:
            new_ing_v = int(input("Enter new Ingredients Quantity"
                                  " (numerical value only): \n"))
            invt_sheet.append_row([new_ing, new_ing_v])
            print(Fore.GREEN + "Inventory successfully updated.\n")
            return_invt_menu()
            break
        except ValueError:
            print(Fore.RED + "Invalid input, numerical value needed.\n")
            add_ingredient()


def user_update_ing():
    """
    Allow user input to update Inventory levels by ensuring a match with
    Inventory items and user's input.
    """
    invt_sheet = SHEET.worksheet("inventory")
    records = invt_sheet.get_all_records()
    # Check that the item is present in Inventory records
    while True:
        ing_c = input("Enter Ingredient name as displayed"
                      " above (include unit eg: (g)): \n")
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
                        cho = input("Update another Ingredient? Enter Y or N.")
                        print("\n")
                        if cho == 'Y' or cho == 'y':
                            clearScreen()
                            print(Back.MAGENTA + Fore.WHITE + Style.BRIGHT +
                                  "*** CURRENT INVENTORY LEVELS ***\n")
                            time.sleep(.5)
                            return_invt_menu()
                        elif cho == 'N' or cho == 'n':
                            return_main()
                        else:
                            print(Fore.RED + "Invalid input.\n")
                            check_invt()
                    except ValueError:
                        print(Fore.RED + "Value must be numerical.\n")
                        continue
        if not record_found:
            print(Fore.RED + "Ingredient not found in Inventory.\n")
            continue


def change_invt_item():
    """
    Change item in Inventory records by user input and update
    Google Sheets
    """
    invt_sheet = SHEET.worksheet("inventory")
    col_vals = invt_sheet.col_values(1)
    ing_o = input("Enter Ingredient name as displayed"
                  " above (include unit eg: (g)): \n")
    if ing_o in col_vals:
        cell = invt_sheet.find(ing_o)
        ing_n = input("Enter the new Ingredient: \n")
        invt_sheet.update_cell(cell.row, cell.col, ing_n)
        print(Fore.GREEN + "Inventory successfully updated.\n")
        return_invt_menu()
    else:
        print(Fore.RED + "Item not found in Inventory.\n")
        change_invt_item()


def clear_invt_item():
    """
    Clear inventory item completely from Google Sheet records
    """
    invt_sheet = SHEET.worksheet("inventory")
    # Search for item in first column values
    col_vals = invt_sheet.col_values(1)
    ing_del = input("Enter Ingredient name as displayed"
                    " above (include unit eg: (g)): \n")
    if ing_del in col_vals:
        cell = invt_sheet.find(ing_del)
        invt_sheet.delete_rows(cell.row)
        print(Fore.GREEN + "Records updated successfully.\n")
        return_invt_menu()
    else:
        print(Fore.RED + "Ingredient not found in Inventory.\n")
        clear_invt_item()


def invt_options():
    """
    Menu to choose between adding ingredient, changing ingredient name
    or updating quantity.
    """
    print(Back.MAGENTA + Fore.WHITE + Style.BRIGHT + "*** INVENTORY MENU ***")
    print("\n")
    print(Fore.CYAN + Style.BRIGHT + "1. Add New Ingredient\n")
    print(Fore.CYAN + Style.BRIGHT + "2. Change Ingredient\n")
    print(Fore.CYAN + Style.BRIGHT + "3. Update Ingredient Quantity\n")
    print(Fore.CYAN + Style.BRIGHT + "4. Clear Ingredient Item\n")
    print(Fore.CYAN + Style.BRIGHT + "5. Return to Main Menu\n")
    while True:
        try:
            choice = int(input("Please choose from the Menu: \n"))
            if choice == 1:
                add_ingredient()
                break
            elif choice == 2:
                change_invt_item()
                break
            elif choice == 3:
                user_update_ing()
                break
            elif choice == 4:
                clear_invt_item()
                break
            elif choice == 5:
                typePrint("Returning to Main Menu...")
                time.sleep(1)
                clearScreen()
                main()
                break
        except ValueError:
            print(Fore.RED + "Invalid input. Enter number for Menu choice.\n")
            time.sleep(1)
            continue


def check_invt():
    """
    Pull Inventory data from Inventory Google Sheet and allow
    user to update levels and amend worksheet
    """
    typePrint("Checking Inventory levels...")
    time.sleep(1)
    clearScreen()
    print(Back.MAGENTA + Fore.WHITE + Style.BRIGHT +
          "*** CURRENT INVENTORY LEVELS ***\n")
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
                invt_options()
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
    Return to program start screen after thanking user.
    """
    typePrint("Thank you for using BakeStock.\n")
    typePrint("Returning to program start...")
    time.sleep(2)
    print("\n")
    print("\n")
    clearScreen()
    prog_start()
    main()


def main():
    """
    Main Menu is displayed with options for user input to progress
    through the application.
    """
    print(Back.MAGENTA + Fore.WHITE + Style.BRIGHT +
          "*** WELCOME TO BAKESTOCK ***\n")
    time.sleep(1)
    typePrint("Please choose from the Menu below.\n")
    time.sleep(1)
    print("\n")
    print(Fore.CYAN + Style.BRIGHT + "1. Sales Menu\n")
    print(Fore.CYAN + Style.BRIGHT + "2. Batch Numbers\n")
    print(Fore.CYAN + Style.BRIGHT + "3. Ingredients Inventory\n")
    print(Fore.CYAN + Style.BRIGHT + "4. Exit\n")
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
            elif choice == 6:
                # Just a small Easter Egg for someone to find!
                print(Fore.CYAN + Style.BRIGHT + """
   ____                                    ?~~bL
  z@~ b                                    |  `U,
 ]@[  |                                   ]'  z@'
 d@~' `|, .__     _----L___----, __, .  _t'   `@j
`@L_,   "-~ `--"~-a,           `C.  ~""O_    ._`@
 q@~'   ]P       ]@[             `Y=,  `H+z_  `a@
 `@L  _z@        d@    *     *    Ya     `-@b,_a'
  `-@d@a'       )@[        o      `VL      `a@@'
    aa~'   ],  .a@'                qqL  ), ./~
    @@_  _z~  _d@[                 .V@  .L_d'
     "~@@@'  ]@@@'        __      )@n@bza@-"
       `-@zzz@@@L        )@@z     ]@@=%-"
         "~~@@@@@bz_    _a@@@@z___a@K
             "~-@@@@@@@@@@@@@@@@@@~"
                `~~~-@~~-@@~~~~~'
                      """)
                print(Fore.CYAN + Style.BRIGHT + "  Here's a yummy croissant!")
                time.sleep(1.5)
                return_main()
        except ValueError:
            print(Fore.RED + "Invalid input. Enter number for Menu choice.\n")
            time.sleep(1)
            continue


# Call main two functions
prog_start()
main()
