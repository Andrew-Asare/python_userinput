import sys
import datetime

first_name = input("What is your name?\n")
last_name = input("What is your last name?\n")
age = int(input("Please enter your age\n"))
salary = float(input("What is your salary?\n"))
DOB = input('Date of Birth\n')
DOB = datetime.datetime.strptime(DOB, "%d/%m/%Y")
post_code = input("What is your postcode?\n")
print(age, salary, DOB, post_code)

print("The data type of first name is", type(first_name))
print("The data type of last name is", type(last_name))
print("The data type of age is", type(age))
print("The data type of salary is", type(salary))
print("The data type of DOB is", type(DOB))
print("The data type of Post Code is", type(post_code))