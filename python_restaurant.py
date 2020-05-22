
# SIMPLEST - Restaurant Waiter Helper



# User Stories

#1

# AS a User I want to be able to see the menu in a formated way, so that I can order my meal.



#2

# AS a User I want to be able to order 3 times, and have my responses added to a list so they aren't forgotten



#3

# As a user, I want to have my order read back to me in formated way so I know what I ordered.



# DOD --- Not necessary - can be done as an extra. Go search what DOD means in scrum

# its own project on your laptop and Github

# be git tracked

# have 5 commits mininum!

# has documentation

# follows best practices



# starter code

menu = ['falafel', 'HuMMus', 'coUScous', 'Bacalhau a Bras']
numbers = [1, 2, 3, 4]
food_and_numbers = [numbers, menu]
food_order = []


for x in menu:
    print(x.lower().capitalize())

print("")
print("Please choose your first dish")
order_1 = input("order 1: ")
food_order.append(order_1)
print("Please choose your second dish")
order_2 = input("order 2: ")
food_order.append(order_2)
print("And finally, please choose your third dish")
order_3 = input("order 3: ")
food_order.append(order_3)

print("")
print("You have ordered {},".format(food_order[0]), "{}".format(food_order[1]), "and {}".format(food_order[2]))







# I need to print each item from the list

# print(menu[0])

# before I print I need to make them all capitalized

#  print everything