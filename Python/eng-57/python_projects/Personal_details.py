import datetime
from datetime import datetime

while True:

    first_name = ''
    last_name = ''
    full_name = first_name + last_name
    print('What is your first and last name?')
    full_name = input()
    if full_name != str:
        raise ValueError("Please enter a name")
    print("Excuse me, what colour are your eyes?")
    eye_colour = input()
    if eye_colour != str:
        raise ValueError("Please input a colour")
    print("What is your hair colour?")
    hair_colour = input()
    if hair_colour != str:
        raise ValueError("Please input a colour")
    print("And finally, if it isn't too personal a question, what is your age please?")
    age = int(input())
    if age != int:
        raise ValueError("Please enter a number, for example 22")


    def birthday(now):
        now = datetime.utcnow().year
        return int(now) - age


    print("Hello, {}!".format(full_name), "Welcome, your age is {}".format(age),
          "you have identified as {},".format(gender), "your eye colour is {}".format(eye_colour),
          "and your hair colour is {}".format(hair_colour))

    print("You said you were {}".format(age), "hence you were born in {}".format(birthday(age)))







