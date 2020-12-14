print("Hi, Welcome to the Lalith Quiz!")
print("Try to get as many questions correct as possible...")

mark = 0
correct_questions = 0
total_questions = 4

question_1 = input("1. What was my first programming language? ").lower()
if question_1 == "python":
    print("Correct!")
    correct_questions += 1
else:
    print("Incorrect")

question_2 = input("2. What is my favorite subject? ").lower()
if question_2 == "math":
    print("Correct!")
    correct_questions += 1
else:
    print("Incorrect")

question_3 = input("3. What is my favorite sport? ").lower()
if question_3 == "basketball":
    print("Correct!")
    correct_questions += 1
else:
    print("Incorrect")

question_4 = input("4. What is my favorite food? ").lower()
if question_4 == "rice":
    print("Correct!")
    correct_questions += 1
else:
    print("Incorrect")

end = "Thank you for playing, you got {} questions correct!".format(correct_questions)
mark = (correct_questions / total_questions) * 100
print(end)
score = "Score: {}%".format(mark)
print(score)

if mark <= 100 and mark >= 50:
    print("Nice! You passed!")
else:
    print("Sorry! You failed!")