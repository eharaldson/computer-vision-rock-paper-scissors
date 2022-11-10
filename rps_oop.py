import cv2
from keras.models import load_model
import numpy as np
import time
import random

class RPS:

    def __init__(self, rounds = 3):
        self.rounds = 3
        self.model = load_model('keras_model.h5', compile=False)
        self.cap = cv2.VideoCapture(0)
        self.data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
        self.class_names = open('labels.txt', 'r').readlines()

    def countdown(self):
        print('Rock ...')
        time.sleep(1)
        print('Paper ...')
        time.sleep(1)
        print('Scissors ...')
        time.sleep(1)
        print('Shoot!')

    def get_prediction(self):

        self.countdown()

        ret, frame = self.cap.read()
        resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
        image_np = np.array(resized_frame)
        normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
        self.data[0] = normalized_image
        prediction = self.model.predict(self.data)

        index = np.argmax(prediction)
        class_name = self.class_names[index][2:-1]
        confidence_score = prediction[0][index]

        print(f'You chose {class_name}')

        return class_name

    def get_computer_choice(self):
        options = ['Rock', 'Paper', 'Scissors']
        return(random.choice(options))

    def get_winner(self, computer_choice, user_choice):
        if (computer_choice == 'Rock' and user_choice == 'Scissors') or (computer_choice == 'Paper' and user_choice == 'Rock') or (computer_choice == 'Scissors' and user_choice == 'Paper'):
            print("You lost")
            return -1
        elif computer_choice == user_choice:
            print("It is a tie!")
            return 0
        else:
            print("You won!")
            return 1

    def play(self):

        computer_wins = 0
        player_wins = 0

        round_num = 1

        while player_wins < 3 and computer_wins < 3:

            # Set up for each round
            time.sleep(1)
            print(f"Round {round_num}")
            time.sleep(2)

            # Get user and computer choice
            user_choice = self.get_prediction()
            computer_choice = self.get_computer_choice()

            # Calculate who won from the choices
            result = self.get_winner(computer_choice, user_choice)

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
            self.play()

game = RPS()

game.play()