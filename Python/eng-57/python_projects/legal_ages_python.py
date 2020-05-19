while True:

    import sys

    print("please enter your age")

    age = int(input())

# - You can vote
    if age < 18:
        print("you are too young to vote")
    elif age >= 18:
        print("you are old enough to vote")

# - You can driver
    if age < 16:
        print("you are too young to drive")
    elif age >= 16:
        print("you are old enough to drive")

# - you can't leagally drink but your mates/uncles might have your back (bigger 16)
    if age >= 18:
        print("you can drink until the cows come home")
    elif age < 18 & age > 16:
        print("you cannot legally drink, but your mates and uncles will sort you out")
    else:
        print("go home to your mommy")

# - Your too young, go back to school!
    if age < 16:
        print("go back to school")

    userInput = input("Enter 'R' to restart or 'X' to exit").capitalize()

    if userInput == "X":
        print('Goodbye.')
        sys.exit(-1)





 #  as a user I should be able to keep being prompted for input until I say 'exit'