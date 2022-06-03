import random

while True:
  handOptions = ["rock","paper","scissors"]

  computer = random.choice(handOptions)
  player = None

  player = input("scissors, paper or rock?:").lower()
  while player not in handOptions:
    print("invalid")
    break
  if player in handOptions:
    if player == computer:
      print("computer:", computer)
      print("player:", (player))
      print("its a tie!")
    
    elif player == "rock":
      if computer == "paper":
        print("computer:", computer)
        print("player",player)
        print("You Lose!")

      if computer == "scissors":
        print("computer:", computer)
        print("player:", player)
        print("You Win!")


    elif player == "paper":
      if computer == "rock":
        print("computer:", computer)
        print("player:", player)
        print("You Win!")

      if computer == "scissors":
        print("computer:", computer)
        print("player:", player)
        print("You Lose!")

    elif player == "scissors":
      if computer == "rock":
        print("computer:", computer)
        print("player:", player)
        print("You Lose!")

      if computer == "paper":
        print("computer:", computer)
        print("player:", player)
        print("You Win!")

    if player != computer:
      break
print("Thanks for playing")