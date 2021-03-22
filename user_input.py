import sys
import datetime

first_name = input("What is your name?\n")
last_name = input("What is your last name?\n")

age = int(input("Please enter your age"))
salary = float(input("What is your salary?"))
DOB = input('Date of Birth')
DOB = datetime.datetime.strptime(DOB, "%d/%m/%Y")
post_code = input("What is your postcode?")
print(age, salary, DOB, post_code)
