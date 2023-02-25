# Write your solution below the starter code
# Follow the instructions in the tab to the right

#import random
import random
# Welcome the user to the game
print("Welcome to rock, paper, scissors. Good luck!")

  # Make a choice for the computer player
  # Get a choice from the user
  # Compare the user and computer choice
  # Print the right message, based on the choices

options = ["Rock" , "Paper" , "Scissors"]
computer = random.choice(options)

player = (input("\nRock, Paper, or Scissors? "))

print("\nThe computer chooses "+computer+"")
  
if player == computer:
  print(f"{player} and {computer}. It's a draw.")

elif (player==options[0]):
  if computer==options[1]:
    print("Paper covers Rock. You lose!")
  else:
    print("Rock smashes Scissors. You win!")

elif (player==options[1]):
  if computer==options[2]:
    print("Scissors cut Paper. You lose!")
  else:
    print("Paper covers Rock. You win!")

elif (player==options[2]):
  if computer==options[0]:
    print("Rock smashes Scissors. You lose!")
  else:
    print("Scissors cut Paper. You win!")

else:
  print("You have to enter Rock, Paper, or Scissors.")
  