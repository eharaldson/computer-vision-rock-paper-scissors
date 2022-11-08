import cv2
from keras.models import load_model
import numpy as np
import time
import random

model = load_model('keras_model.h5', compile=False)
cap = cv2.VideoCapture(0)
data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
class_names = open('labels.txt', 'r').readlines()

def get_prediction():

    print('Rock ...')
    time.sleep(1)
    print('Paper ...')
    time.sleep(1)
    print('Scissors ...')
    time.sleep(1)
    print('Shoot!')

    ret, frame = cap.read()
    resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
    image_np = np.array(resized_frame)
    normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
    data[0] = normalized_image
    prediction = model.predict(data)

    index = np.argmax(prediction)
    class_name = class_names[index][2:-1]
    confidence_score = prediction[0][index]

    print(f'You chose {class_name}')

    return class_name

def get_computer_choice():
    options = ['Rock', 'Paper', 'Scissors']
    return(random.choice(options))

def get_winner(computer_choice, user_choice):
    if (computer_choice == 'Rock' and user_choice == 'Scissors') or (computer_choice == 'Paper' and user_choice == 'Rock') or (computer_choice == 'Scissors' and user_choice == 'Paper'):
        print("You lost")
        return -1
    elif computer_choice == user_choice:
        print("It is a tie!")
        return 0
    else:
        print("You won!")
        return 1

def play():

    computer_wins = 0
    player_wins = 0

    round_num = 1

    while player_wins < 3 and computer_wins < 3:

        # Set up for each round
        time.sleep(1)
        print(f"Round {round_num}")
        time.sleep(2)

        # Get user and computer choice
        user_choice = get_prediction()
        computer_choice = get_computer_choice()

        # Calculate who won from the choices
        result = get_winner(computer_choice, user_choice)

        # Update score
        if result == 1:
            player_wins += 1
        elif result == -1:
            computer_wins += 1

        round_num += 1
    
    if player_wins == 3:
        print("Congratulations you won the game!")
    else:
        print("Sorry, the computer won the game.")

    play_again = input("Would you like to play another game? (y/n) ")

    if play_again == 'y':
        play()

play()

# Release the cap object
cap.release()
# Destroy all the windows
cv2.destroyAllWindows()