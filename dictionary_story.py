# Dictionary basics :D

#1 - Define a dictionary call story1, it should have the followign keys:
        # 'start', 'middle' and 'end'

#2 - Print the entire dictionary

#3 - Print the type of your dictionary

#4 - Print only the keys

#4 - print only the values

#5 - print the individual values using the keys (individually, lots of printi commands)

#6 - Now let's add a new key:value pair.
    # 'hero': yourSuperHero

story1 = {'start': 'Spider_builder', 'middle': 'forgot', 'end': 'his hod'}
print(story1)
print(type(story1))

for item in story1:
    print('{}'.format(item, story1[item]))

for item in story1:
    print(story1[item])

print(story1.get('start'))
print(story1.get('middle'))
print(story1.get('end'))


[print(item) for item in story1.items()]

story1['hero'] = 'Iron Man'

print(story1)
[print(item) for item in story1.items()]

