print("Hi, Welcome to the Lalith Quiz!")
print("Try to get as many questions correct as possible")

score = 0
total_questions = 5

ans = input("1. What is my first Programming Language? ").lower()

if ans == "python":
    print("Correct!")
    score += 1
else:
    print("Incorrect")

ans = input("2. What is my favourite color? ").lower()

if ans == "blue":
    print("Correct")
    score += 1
else:
    print("Incorrect")

ans = input("3. What is my favourite sport? ").lower()

if ans == "basketball" or "soccer":
    print("Correct")
    score += 1
else:
    print("Incorrect")


ans = input("4. Who is my sibling? ").lower()

if ans == "vaishnavi":
    print("Correct")
    score += 1
else:
    print("Incorrect")

ans = input("5. What is my family's lastname? ").lower()

if ans == "bandaru":
    print("Correct")
    score += 1
else:
    print("Incorrect")

print("Thank you for playing, you got", score, "questions correct!")

mark = (score/total_questions) * 100

print("Mark: ", mark, "%")
print("Goodbye")