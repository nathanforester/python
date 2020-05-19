# Magic number game!

# I want you to use operators

# equate something
import random
import math



# As a user, I want to be able to guess a number and know if i got it correct or not, so that I can know if I won or not.



while True:

# We should define/assign number to a variable called magic_number

    magic_number = (random.randint(0, 5))



# I need to ask user for input
    print("please enter a number between 1 and 5")
    user_input = int(input())






# I need to check if this input matches a magic_number

    if user_input == magic_number:
        print("your response was correct")
    else:
        print("sorry, your response was incorrect")




# I need to let the user know if the response was write or not
