import gspread
from google.oauth2.service_account import Credentials
import random

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('snowman')

scores = SHEET.worksheet('scores')
easywords = SHEET.worksheet("easy")
modwords = SHEET.worksheet("moderate")
hardwords = SHEET.worksheet("hard")



# Main Game

def menu():
    print("Main Menu:\n")
    print("1 Instructions\n")
    print("2 Play Game\n")

    while True:
        menu_option = input("Choose from menu: ")
        if menu_option == "1":
            return instructions()
        elif menu_option == "2":
            return play_game()
        else:
            print("Please choose 1 or 2")
       


def instructions():
    print("instructions here")


def play_game():
    print("\n Difficulty level\n")
    print("1 Easy\n")
    print("2 Moderate\n")
    print("3 Hard\n")

    while True:
        menu_option = input("Choose difficulty level: ")
        if menu_option == "1":
            words = easywords.get_all_values() 
            start_game(words)
            break 
        elif menu_option == "2":
            words = modwords.get_all_values()
            start_game(words)
            break 
        elif menu_option == "3":
            words = hardwords.get_all_values() 
            start_game(words)
            break   
        else:
            print("Please choose 1,2 or 3")


def start_game(words):
    currentword = random.choice(words)
    print(currentword)

menu()