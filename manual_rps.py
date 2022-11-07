import random

options = ['Rock', 'Paper', 'Scissors']

def get_computer_choice():
    return(random.choice(options))

def get_user_choice():
    while True:
        user_choice = input('Rock... Paper... Scissors... Shoot: ')
        if user_choice not in options:
            print('Please enter a valid input')
