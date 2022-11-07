import random

options = ['Rock', 'Paper', 'Scissors']

def get_computer_choice():
    return(random.choice(options))

def get_user_choice():
    while True:
        user_choice = input('Rock... Paper... Scissors... Shoot: ')
        if user_choice not in options:
            print('Please enter a valid input')
        else:
            return user_choice

def get_winner(computer_choice, user_choice):
    if (computer_choice == 'Rock' and user_choice == 'Scissors') or (computer_choice == 'Paper' and user_choice == 'Rock') or (computer_choice == 'Scissors' and user_choice == 'Paper'):
        print("You lost")
    elif computer_choice == user_choice:
        print("It is a tie!")
    else:
        print("You won!")

def play():

    computer_choice = get_computer_choice()
    user_choice = get_user_choice()

    get_winner(computer_choice, user_choice)

play()