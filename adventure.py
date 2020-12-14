print("Welcome to my adventure game!")
ans = input("Would you like to play (yes/no)? ").lower()
print("Game Started!")
health = 15

if ans == "yes":
    print("You will be starting off with 15 health")
    print("Let's Play!")

    pathways = input("You notice there are two pathways... Do you want to go left or go right (left/right)? ").lower()
    if pathways == "left":
        print("You took the left path.")
        first = input("You notice a road... Do you want to use the sidewalk to cross or go across the road (sidewalk/across)? ").lower()

        if first == "sidewalk":
            print("You decide to cross the road using the sidewalk and crossed the road safely.")
        elif first == "across":
            print("You decide to go across the road to cross the road, but you got hit by a car and lost 5 health.")
            health -= 10
            
        second = input("You see a strange animal... Do you want to pet it or just leave it alone (pet/alone)? ").lower()

        if second == "alone":
            print("You decide to leave it alone, so it will not mess with you.")
        elif second == "pet":
            print("You decide to pet it, but it got scared and decided to bite you, so you lost 5 health.")
            health -= 5
            
        third = input("You see a river... Do you want to go across or go around (across/around)? ").lower()

        if third == "around":
            print("You decided to go around the river, so you reach your house, which means You win!")
        elif third == "across":
            print("You managed to get across, but you were bitten by a fish and lost 5 health, You Lost!")
            health -= 0
    else:
        print("You took the right path and fell down a hole and lost.")

else:
    print("Goodbye!")
