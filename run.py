# Settings and credentials to allow access, read and modify data in
# Google Sheets
import gspread
from google.oauth2.service_account import Credentials


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


def prog_start():
    """
    Run opening screen for user and display menu options for user.
    """
    print('''
    *********************************************************************
    
    88888b.          88              .d888b.   88                  88      
    88  "88b         88             d88P  Y88b 88                  88      
    88  .8P          88             Y88b.      88                  88      
    88888K.    888b. 88  88  .d88b.  "Y88b.    8888 .d88b.  .d888b 88  88 
    88  "Y8b    "88b 88 .8P d8P  Y8b   "Y88b.  88   d8""8b d8P"    88 .8P 
    88    88 .d88888 88888K 8888888"     "888  88   88  88 88      88888K  
    88   d8P 888  88 88 "8b Y8b.    Y88b  d88P Y8b. Y8..8P Y8b.    88 "8b 
    888888P" "Y88888 88  88  "Y8888  "Y888P"   "Y88."Y88P"  "Y888P 88  88

    *********************************************************************
    ''')