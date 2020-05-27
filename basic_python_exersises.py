# Practice string

# Welcome to Sparta - exercise
from datetime import datetime


name = input('what is your first name? ')

print("hello, {}".format(name))
# first_name = input("please enter your first name")
last_name = input("please enter your last name ")
full_name = name + ' ' + last_name
print("Welcome, {}".format(full_name).strip())
age = int(input("What is your age? "))


def birthday(now):
    now = datetime.utcnow().year
    return int(now) - age


print("OMG {},".format(full_name), "you are {}".format(age), ",so you were born in {}".format(birthday(age)))

# comment added so git status can be changed

