import sys
import datetime

first_name = input("What is your name?\n")
last_name = input("What is your last name?\n")

age = int(input("Please enter your age\n"))
salary = float(input("What is your salary?\n"))
DOB = input('Date of Birth\n')
DOB = datetime.datetime.strptime(DOB, "%d/%m/%Y\n")
post_code = input("What is your postcode?\n")
print(age, salary, DOB, post_code)

print(type(age))
print(type(salary))
print(type(DOB))
print(type(post_code))