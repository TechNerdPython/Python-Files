#ages = [10, 41, 55, 18, 20, 11]

# for age in ages:
# if age > 17:
#print("This person with this age: "+ str(age), "is an adult")
# if age < 17:
#print("This person with this age: " + str(age), "is not an adult")

#grades = [55, 65, 85, 90, 75, 100, 98, 95]

# for grade in grades:
# if grade < 70:
#    print("This person with this grade: " + str(grade), "got a C on the test.")
# elif grade >=70 and grade <=80:
#    print("This person with this grade: " + str(grade), "got a B- on the test.")
# elif grade > 80 and grade <=90:
#    print("This person with this grade: " + str(grade), "got a B+ on the test.")
# elif grade >90:
# print("This person with this grade: " + str(grade), "got a A+ on the test.")

#grades = [90, 95, 99, 100]
#names = {90:"Rajesh", 95:"Prema", 99:"Lalith", 100:"Vaishnavi"}

# for grade in names:
# if grade >=70 and grade <= 90:
#    print("This person named: " + str(names[grade] + " and grade is:" +str(grade)))
# if grade >=91 and grade <= 95:
#    print("This person named: " + str(names[grade]))
# if grade >=96 and grade <= 99:
#    print("This person named: " + str(names[grade]))
# if grade >=100:
#    print("This person named: " + str(names[grade]))

#names = {43: "Rajesh", 33: "Prema", 14: "Lalith", 8: "Vaishnavi", 55: "Srinivas Rao"}

# for age in names:
# if age > 5 and age < 10:
#    print("This person's name is: " + str(names[age]) + " the age is: " + str(age))
# elif age > 10 and age < 18:
#    print("This person's name is: " + str(names[age]) + " the age is: " + str(age))
# elif age > 30 and age < 35:
#    print("This person's name is: " + str(names[age]) + " the age is: " + str(age))
# elif age > 40 and age < 45:
#    print("This person's name is: " + str(names[age]) + " the age is: " + str(age))
# else:
#    print("There is no name included in the list with the parameters given.")

# import datetime
# import pytz

#today = datetime.date.today()
# print(today)

#birthday = datetime.date(2006, 8, 15)
# print(birthday)

#days_since_birth = today - birthday
# print(days_since_birth)

# def square_number(a, b):
#    return a ** b
#print(exp(4, 2))

#nums = [2, 5, 10, 15, 18, 20, 25, 8]
# print(sorted(nums))
#print(sorted(nums, reverse=True))

#myfile = open("textfile.txt", "w")
#myfile.write("Lalith likes to do Math and Code Python\n Lalith is a Math Nerd\n Lalith likes Rice and Samosas")
# myfile.close()

#myfile = open("textfile.txt", "r")
# print(myfile.read())

#myfile = open("textfile.txt", "w")

#myfile.write("Lalith likes to do Math and Code Python\n Lalith is a Math Nerd\n Lalith likes to eat Rice and Samosas")

#myfile = open("textfile.txt", "r")
# print(myfile.read())
# myfile.close()

#myfile = open("testfile.txt", "w")

#myfile.write("VAISHU DOES HIAH EVERYDAY!, PLEASE HELP ME!!")

#myfile = open("testfile.txt", "r")
# print(myfile.read())
# myfile.close()

#myfile = open("vaishu.txt", "w")

#myfile.write("VAISHU DOES HIAH EVERYDAY!, PLEASE HELP ME!!")

#myfile = open("vaishu.txt", "r")
# print(myfile.read())
# myfile.close()

#myfile = open("vaishu.txt", "w")
#myfile.write("VAISHU DOES OII EVERYDAY TOO")

#myfile = open("vaishu.txt", "r")
# print(myfile.read())
# myfile.close()

#myfile = open("groceries.txt", "w+")

#myfile.write("Tomatoes\n Beans\n Carrots\n Dosakai Squash\n Sorakaya\n Beerakay\n Okra\n Tindora\n")

#myfile = open("groceries.txt", "r")

# print(myfile.read())

#import time

#run = input("Start? >")

#seconds = 0

# if run == "yes":
# while seconds !=10:
#    print(">", seconds)
#    time.sleep(1)
#    seconds += 1
#print(">", seconds)

#ages = [10, 41, 55, 18, 20, 11]
# length=len(ages)
# p=1
# for i in range(length):
#    print (ages[i])
#    o=i
#    p +=i
#    m=ages[o]
#    j=ages[p]
#    print(o,p)
#    if (m<=j):
#        k=m;
#    else:
#        k=j;
# print(k)

#numbers = [0, 1, 5, 8, 6]

# if numbers[0] > numbers[1]:
#    print(numbers[1], numbers[0])
# if numbers[1] < numbers[2]:
#    print(numbers[1], numbers[2])
# if numbers[3] > numbers[4]:
#    print(numbers[4], numbers[3])

# def get_prime_factors(N):
#    factors = list()
#    divisor = 2
#    while(divisor <= N):
#        if (N % divisor) == 0:
#            factors.append(divisor)
#            N = N/divisor
#        else:
#            divisor += 1
#    return factors

#from string import Template

#str1 = ("Lalith likes to do {0} and Code {1}.").format("Math", "Python")
# print(str1)

#str2 = ("Lalith likes to do {subject} and Code {language}.").format(subject="Math", language="Python")
# print(str2)

#templ = Template("Lalith likes to do ${subject} and Code ${language}.")

# data = {
#    "subject" : "Math",
#    "language" : "Python"
# }

#result = templ.substitute(data)

# print(result)

# import collections

# Number = collections.namedtuple("Number", "a b")

# n1 = Number(1, 2)
# n2 = Number(5, 6)

# print(n1, n2)

# print(n1.a, n2.b)

# n1 = n1._replace(a=25)
# print(n1)

# import requests
# def printResults(resData):
#     print("Result code: {0}".format(resData.status_code))

#     print("Headers: ------------------")
#     print(resData.headers)

#     print("Returned Data: ---------------")
#     print(resData.text)

# url = "http://httpbin.org/json"

# result = requests.get(url)
# printResults(result)

# name = input("What is your name: ")
# age = int(input("How old are you: "))
# year = str((2020 - age)+100)
# print(name, "will be 100 years old in the year of: " + str(year))

# number = int(input("What is your number: "))

# if number % 2:
#     print("The number " + str(number), "is an odd number")
# else:
#  print("The number" + str(number), "is an even number")

import requests
from requests.auth import HTTPBasicAuth


def printResults(resData):
    print("Result code: {0}".format(resData.status_code))

    print("Headers: ------------------")
    print(resData.headers)

    print("Returned Data: ---------------")
    print(resData.text)


url = "http://httpbin.org/get"

data = {
    "Name": "Lalith",
    "Age": 14
}
result = requests.get(url, data=data)
# printResults(result)

url = "http://httpbin.org/basic-auth/Lalith123/Lbandaru389281!"

myCreds = HTTPBasicAuth("Lalith123", "Lbandaru389281!")

result = requests.get(url, auth=myCreds)
# printResults(result)

# def fizz_buzz(number):
#     if (number % 5 ==0) and (number % 3 ==0):
#         print("FizzBuzz")
#     elif (number % 3) == 0:
#         print("Fizz")
#     elif (number % 5) == 0:
#         print("Buzz")
#     else:
#         print(number)

# number = int(input("Choose a number: "))

# fizz_buzz(number)

# num1 = int(input("Enter your first number: "))
# num2 = int(input("Enter your second number: "))
# print(num1 * num2)

# def sum_of_number(num):
#     previousNum = 0

#     for i in range(num):
#         sum = previousNum + i
#         print("Current Number: ", i, "Previous Number: ", previousNum, "Sum: ", sum)
#         previousNum = i
# sum_of_number(20)

# list1 = [10, 20, 30, 40, 10]
# print("Given list: ",list1)
# first_element = list1[0]
# last_element = list1[4]
# if first_element == last_element:
#     print(True)
# else:
#     print(False)

# list = [25, 36, 15, 23, 50]
# print("Given list: ", list)
# for num in list:
#     if num % 5 == 0:
#         print("The number: ",num, "is divisible by 5")
#     else:
#         print("The number: ",num, "is not divisible by 5")

# def sleep_in(weekday, vacation):
#     if weekday == False or vacation == True:
#         return True
#     else:
#         return False

# print(sleep_in("Friday", "False"))

# def monkey_trouble(a_smile, b_smile):
#     if a_smile or b_smile:
#         return True
#     if not a_smile or not b_smile:
#         return True
#     else:
#         return False

# print(monkey_trouble(False, True))

# def sum_double(a, b):
#     sum =  a + b

#     if a == b:
#         sum = sum * 2
#         return sum

# print(sum_double(3, 2))

# myfile = open("textfile.txt", "r")

# myfile.write("This is line 7\n")

# myfile = open("textfile.txt", "r")
# print(myfile.read())

# def makes10(a, b):
#     if a + b == 10:
#         return True
#     if a == 10 or b == 10:
#         return True
#     if a + b != 10:
#         return False

# print(makes10(10, 1))

# def near100(n):
#     return ((abs(100 - n) <= 10) or (abs(200 - n) <= 10))

# def string_times(str, n):
#     return str * n

# print(string_times("Lalith", 2))

# try:
#     f = open("textfile.txt")
#     print(f)

# except Exception:
#     print("Error!, File not found.")

# else:
#     print("No Error, File found")

# def hello_name(name):
#     return "Hi " + name + !

# print(hello_name("Lalith"))

# def sum3(nums):
#     return sum(nums)

# print(sum3([7, 0, 0]))

