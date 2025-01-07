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

scores = SHEET.worksheet("scores")
easywords = SHEET.worksheet("easy")
modwords = SHEET.worksheet("moderate")
hardwords = SHEET.worksheet("hard")

# Main Game

def getscores():
    getscores = scores.get_all_values()
    allscores = getscores[1:]
    scores_list=(allscores[0])
    #Currentscore, PersonalHighScore, and Current(overall)HS from google sheet
    cus = scores_list[0]
    phs = scores_list[1]
    chs = scores_list[2]

#def update_scores():
    #scores.update('A2', [[cus, phs, chs]])
    


def snowman(incorrect):
    if incorrect==0:
        print("~~~~~~~~~~~~~~~~")
    elif incorrect==1:
        print("    (   *  )    ")
        print("~~~~~~~~~~~~~~~~")
    elif incorrect==2:
        print("     (  * )     ")
        print("    (   *  )    ")
        print("~~~~~~~~~~~~~~~~")
    elif incorrect==3:
        print("      (  )      ")
        print("     (  * )     ")
        print("    (   *  )    ")
        print("~~~~~~~~~~~~~~~~")
    elif incorrect==4:
        print("      (  )      ")
        print("   --(  * )--   ")
        print("    (   *  )    ")
        print("~~~~~~~~~~~~~~~~")
    elif incorrect==5:
        print("       __       ")
        print("     _|__|_     ")
        print("      (  )      ")
        print("   --(  * )--   ")
        print("    (   *  )    ")
        print("~~~~~~~~~~~~~~~~")
    elif incorrect==6:
        print("       __       ")
        print("     _|__|_     ")
        print("      (*-)      ")
        print("   --(  * )--   ")
        print("    (   *  )    ")
        print("~~~~~~~~~~~~~~~~")

def menu():
    score=0
    print("Main Menu:\n")
    print("1 Instructions\n")
    print("2 Play Game\n")

    while True:
        menu_option = input("Choose from menu: \n")
        if menu_option == "1":
            return instructions()
        elif menu_option == "2":
            return choose_hard()
        else:
            print("Please choose 1 or 2")

def instructions():
    print("instructions here")


def choose_hard():
    print("\nDifficulty level\n")
    print("1 Easy\n")
    print("2 Moderate\n")
    print("3 Hard\n")

    while True:
        menu_option = input("Choose difficulty level: \n")
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
    print("\nLet's play!\n")
    currentguess = "-" * len(currentword)
    incorrect = 0
    attempts = 6
    print(currentguess)

    # Loop until the word is guessed or attempts run out:
    while "-" in currentguess and attempts > 0:  
        guess = input("\nPlease choose a letter\n")

        # Check input validity
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single valid letter.\n")
            # Restart the loop for valid input
            continue  

        # check guess
        if guess in currentword:
            print("Well done!\n")

            # Update word revealing correct letters
            for i in range(len(currentword)):
                if guess == currentword[i]:
                    currentguess = currentguess[:i] + guess + currentguess[i+1:]
                    print(f"{currentguess}\n")
        else:
            print("Sorry, wrong letter\n")
            incorrect += 1
            attempts -=1
        snowman(incorrect)

    if "-" in currentguess:
        result = "lost"
    else:
        result = "won"
        #score +=1

    #update_scores()

    print(f"Game over. You {result}. \n")
    #need to come back and sort this out later when done the won/lost

    again = input("Play again? Y or N: \n")
    if again.upper() == "Y":
        choose_hard()
    elif again.upper() == "N":
        print("Thanks for playing!")
    else: 
        print("Please enter Y or N: ")

def main():
    getscores()
    menu()

main()