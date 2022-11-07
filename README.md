# Computer Vision Rock Paper Scissors

## Milestone 1
- Git is a VCS (Version Control System) which can utilised distributed version control along with GitHub to track changes to files, collaborate with others, display code publicly for others to read/use, and revert to old version of a codebase. These technologies are used widely in industry as they allow for safe collaboration on software projects with multiple people.

## Milestone 2
- I created an image model on teachable machine for 4 different classes: Nothing, Rock, Paper, and Scissors. The model is a pretrained neural network with the images I provided becoming the last layer of the network.

## Milestone 3
- A manual game of Rock, Paper, Scissors was created where the camera and ML model is not used. It uses the random module to get the computer's choice and uses the input function to get the choice from the player. The game consists of a play() function that is called to start the game. In this function the script calls get_computer_choice and get_user_choice to get the choices of the two players and calculates a winnner using the get_winner function. The latter function has the rules of the game hardcoded to print whether the computer or the player has won the game. This is all found in the manual_rps.py script.