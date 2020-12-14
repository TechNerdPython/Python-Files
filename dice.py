import random
import time

while True:
    ans = input("Do you want to roll the dice (y/n)? ")

    if ans == "n":
        exit()
    elif ans == "y":
        print("\nRolling the Dice...")
        time.sleep(1)

        dice_1 = random.randint(1, 6)
        dice_2 = random.randint(1, 6)

        print("The values are: ")
        print("Dice 1 = ", dice_1, "\nDice 2 = ", dice_2)

    if dice_1 == dice_2:
       print("The values are: ")
       print("Dice 1 = ", dice_1, "\nDice 2 = ", dice_2)
       print("You rolled a double!")