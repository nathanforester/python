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
    print('{}'.format(item, story1[item])) ## returns keys

for item in story1:  ## returns values
    print(story1[item])

for key in story1.keys(): ## returns all keys
    print(key)

for value in story1.values(): ## returns all values
    print(value)

print(story1.get('start')) ## returns values individually
print(story1.get('middle'))
print(story1.get('end'))


[print(item) for item in story1.items()]

story1['hero'] = 'Iron Man' ## add key and value (append)

print(story1)
[print(item) for item in story1.items()] ## returns all keys and values together


print(story1.keys()) ## returns all keys and all values
print(story1.values())

print(story1['start']) ## returns values
print(story1['middle'])
print(story1['end'])
print(story1['hero'])

for item in story1:
    print(item) # # returns keys