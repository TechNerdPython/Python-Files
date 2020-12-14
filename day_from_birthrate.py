import datetime

date = str(input("Enter your birthdate: "))

day_names = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

day = datetime.datetime.strptime(date, "%m %d %Y").weekday()

print(day_names[day])