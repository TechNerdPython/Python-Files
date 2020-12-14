from random import randint

choices = ["Rock", "Paper", "Scissors"]
print("Welcome to the Rock, Paper, Scissors Game!")
computer = choices[randint(0,2)]

while True:
    player = input("Your move: (Rock/Paper/Scissors)? ")
    print("Computer chose: ",computer)
    if player == computer:
        print("Draw")
    elif player == "Rock" and computer == "Paper":
        print("Paper takes Rock")
    elif player == "Rock" and computer == "Scissors":
        print("Rock takes Scissors")
    elif player == "Paper" and computer == "Rock":
        print("Paper takes Rock")
    elif player == "Paper" and computer == "Scissors":
        print("Scissors takes Paper")
    elif player == "Scissors" and computer == "Rock":
        print("Rock takes Scissors")
    elif player == "Scissors" and computer == "Paper":
        print("Scissors takes Paper")    