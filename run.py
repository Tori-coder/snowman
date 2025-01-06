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
            words = [item for sublist in easywords.get_all_values() for item in sublist] 
            start_game(words)
            break 
        elif menu_option == "2":
            words = [item for sublist in modwords.get_all_values() for item in sublist]
            start_game(words)
            break 
        elif menu_option == "3":
            words = [item for sublist in hardwords.get_all_values() for item in sublist]
            start_game(words)
            break   
        else:
            print("Please choose 1,2 or 3")


def start_game(words):
    currentword = random.choice(words)
    print("Let's play!\n")
    currentguess = "-" * len(currentword)
    print(currentguess)
    print("\n")
    guess = input("Please choose a letter\n")

    # check guess
    if guess in currentword:
        print("Well done!\n")

        #  Updates word revealing correct letters
        for i in range(len(currentword)):
            if guess == currentword[i]:
                currentguess = currentguess[:i] + guess + currentguess[i+1:]
                print(currentguess)
    
    else:
        print("Sorry, wrong letter\n")
     

menu()