# Write a bizz and zzuu game ##project

# as a user I should be able prompted for a number, as the program will print all the number up to and inclusing said number while following the constraints / specs. (bizz and buzz for multiples or 3 and 5)

# As a user I should be able to keep giving the program different numbers and it will calculate appropriately until you use the key word: 'penpinapplespen'


# write a program that take a number
# prints back each individual number, but
    # if it is a multiple of 3 it returns bizz
    # if a multiple of 5 it return zzuu
fizz_buzz_numbers = ''
print('please enter a number')

while fizz_buzz_numbers != 'penpinapplespen':

    fizz_buzz_numbers = input()
    if fizz_buzz_numbers == 'penpinapplespen':
        print('Thank you for playing, goodbye! ')
        break

    fizz_buzz_numbers = int(fizz_buzz_numbers)
    for fizz_buzz_numbers in range(1, fizz_buzz_numbers+1):
        if fizz_buzz_numbers % 3 == 0:
            print("bizz")
        elif fizz_buzz_numbers % 5 == 0:
            print("zzuu")
        else:
            print(fizz_buzz_numbers)

    print('enter another number or type the secret password to exit')



























