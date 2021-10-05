import random

# problem 1
day_of_week = 'monday'
print(day_of_week)
day_of_week = 'friday'
print(f"I can't wait for {day_of_week}")





#problem 2
animal_input = input('What is your favorite animal?')
color_input = input('What is your favorite color?')
print(f"I've never seen a {color_input} {animal_input}")






#conditionals
#favorite breakfast is eggs, lunch is ruben, and dinner is chicken pasta
time_of_day = 1100
favorite_meal_for_time = ''
meal_of_day=''
if time_of_day <1200:
    meal_of_day = 'Eggs for breakfast'
elif time_of_day > 1200 and time_of_day <1700:
    meal_of_day = 'Ruben for lunch!'
else:
    meal_of_day = 'chicken pasta is for dinner!'
print(meal_of_day)





#random number
random_number= random.randint(0,10)
if random_number < 3:
    print('Beatles')
elif random_number > 2 and random_number <6:
    print('Stones')
elif random_number > 5 and random_number < 9:
    print('Floyd')
else:
    print('Hendrix')
print(random_number)





# for loop iterating a certain number of times
for thing in range(7):
    print('python is cool!')
number=0
for number in range(11):
    print(number)
    number += 1
for word in range(5):
    print('hello'+'\n'+ 'goodbye')





# while loops make sure to end loop somehow
height = 40
while height < 48:
    print('you cant ride this ride')
    height += 1





#magic number!
magic_number = 50
guess = input('guess the magic number')
guess_int = int(guess)
while guess_int:
    if guess_int == magic_number:
        print(f'{magic_number} is the magic number!')
        break
    if guess_int < magic_number:
        guess = input('too low, try again')
        guess_int = int(guess)
    if guess_int > magic_number:
        guess = input('too high, try again')
        guess_int = int(guess)
    if guess_int in range(magic_number-10, magic_number+10):
        print('getting warmer')





# favorite movie void function
def print_movie_name():
    my_favorite_movie= 'kill bill'
    print(my_favorite_movie)

print_movie_name()






#favorite band
def user_favorite_band():
    band_input = input('what is your favorite band')
    return band_input

users_band = user_favorite_band()
print(users_band)

# concert_display(users_band)
def concert_display(musical_act):
    my_street = input('what street do you live on?')
    print(f'it would be great if {musical_act} played on {my_street}.')






#desktop items

desktop_items = ['tablet', 'phone', 'computer']
print(desktop_items[1])
desktop_items.append('infinity gauntlet')
for items in desktop_items:
    print(items)