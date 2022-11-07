import random

options = ['Rock', 'Paper', 'Scissors']

def get_computer_choice():
    return(random.choice(options))

def get_user_choice():
    while True:
        user_choice = input('Rock... Paper... Scissors... Shoot: ')
        if user_choice not in options:
            print('Please enter a valid input')

def get_winner(computer_choice, user_choice):
    if (computer_choice == 'rock' and user_choice == 'scissors') or (computer_choice == 'paper' and user_choice == 'rock') or (computer_choice == 'scissors' and user_choice == 'paper'):
        print("You lost")
    elif computer_choice == user_choice:
        print("It is a tie!")
    else:
        print("You won!")