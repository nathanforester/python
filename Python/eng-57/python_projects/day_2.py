import time

# single_quotes = 'single quotes'
# print(single_quotes)
#
# double_quotes = "Martin's double quotes"
# print(double_quotes)
#
# string_fixed = 'I said \'wow!\''
#
# quote_in_quote = 'I said "wow!"'
# print(string_fixed)
# print(quote_in_quote)

# slicing strings

# h e l l o w o r l d !
# 0 1 2 3 4 5 6 7 8 9 0 10 11

# Hw = 'Hello, world!'
# print(Hw[7:])
# print(Hw[:7])
# print(Hw[0:5])
# print(Hw[8:])
# print(len(Hw))
# a = 234545
# print(a)
# a = [2, 3, 4, 5]
# print(a[2])

# strip
# white_space = "lot's of space      "
# print(len(white_space))
#
# print(len(white_space.strip()))
# how to strip from middle?

# # some more methods
# Example_text = "some text here"
# print(Example_text.count("text")) # counts the instance of the string appearing

# Bring everything to?
# Example_text = "SHOUTING CAPS!"
# print(Example_text.lower())
# how to replace a string ?

# BRING EVERYTHING TO UPPERCASE
# Example_text = "whispering"
# print(Example_text.upper())
#
# Example_text = "shouting first capital"
# print(Example_text.title())
#
# Example_text = "some text here"
# print(Example_text.capitalize())
#
# Example_text = "some text"
# print(Example_text.replace("some", "plenty of"))
#
# # concatenation & casting
# Example_text = "here's some text"
# Example_text_1 = " and here is some more text"
#
# x = 2
# y = 5.4
# z = "there's now a number 24.5 unless we put a space in"
# print(z, ' ', float(x + y))
# print(z, ' ', str(x + y))
# print(z + " " + str(y) + " " + str(x) + " " + str(x+y))
# res = y + float(x)
# x = "2"
# print(type(x))
# print(int(x) + res)
#
# x = "6"

# a = True
# b = False
# c = 2
# d = 1
# if c == d:
#     print(a)
# else:
#     print(b)
#
# if c != d:
#     print(a)
# else:
#     print(b)
#
# print(c == d)
# print(c <= d)
# print(c >= d)

#
# Greetings = "Hello, world!"
# print(Greetings.startswith("H"))
# print(Greetings.startswith("r"))
# print(Greetings.endswith("!"))
# print(Greetings.endswith("donkey"))
# print(bool(a))
# print("" == None)

# lists, tuples, (maybe dictionaries)
# lists are exactly what you expect. They are lists.
# they are organised with index. This means they start at 0.
# lists can hold any data type
# array values are mutable
# my_stingy_landlords = ['Bill', 'Trudy', 'Voldermort', 'hotel of mum and dad']
# index = [0, 1, 2]
# print(type([]))
# print(len([]))
# print(my_stingy_landlords)
# print(my_stingy_landlords[0])
# special_landlord = my_stingy_landlords[2]
# print(special_landlord)
# print(my_stingy_landlords[-1])

# re-assign an entry
# my_stingy_landlords[0] = "Swansea University"
# print(my_stingy_landlords[0])
# my_stingy_landlords = ['Bill', 'Trudy', 'Voldermort', 'hotel of mum and dad']
# index = [0, 1, 2, 3]

# Remove an entry from a list remove
# my_stingy_landlords.remove('hotel of mum and dad')
# my_stingy_landlords.append('Nathan')
# del my_stingy_landlords[-1]
# my_stingy_landlords.append('Filipe')
# print(my_stingy_landlords[3])
# my_stingy_landlords.pop(-1)
# my_stingy_landlords.append('Mr.Flat')
# print(my_stingy_landlords)
# my_stingy_landlords.insert(3, 'Mr.Flat')
# print(my_stingy_landlords[-1])


# add an entry to a list insert or append
# Nathan

# Remove entry and index del

# new_list = []
#
#
# def iterate_through_list():
#     for item in list:
#         new_list.append()

# control flow dictates where the code will flow
# much like dance in real life
# in coding we do this with if functions and while loops

# if functions
# if functions work with booleans with true or false and comparison operators to equate and compare objects
# result in true or false booleans

# syntax
# if <condition>
#    run <block of code> - block is a section of code that runs
# elif <2nd condition>
# else <no code>
# return

# logical and, logical or
# condition
weather = input("What is the weather today?")
is_rainy = True
safety_alert = 'red'

if is_rainy:
    time.sleep(2)
    print('umbrella')
elif weather == "stormy":
    print("stay at home")
else:
    print("use factor 50")
elif weather == 'stormy' AND safety_alert = 'red:'


















