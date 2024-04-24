import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
           'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G',
           'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print('Hello..! Welcome to password generator')
nr_letters = int(input('How many letters do you want in your password ? \n'))
nr_numbers = int(input('How many numbers do you want in your password ? \n'))
nr_symbols = int(input('How many symbols do you want in your password ? \n'))

password = ''
for letter in range(1,nr_letters+1):
    password += random.choice(letters)
for number in range(1,nr_numbers+1) :
    password += random.choice(numbers)
for symbol in range(1,nr_symbols+1):
    password += random.choice(symbols)

print(f'first password is {password}')

password_char = []

for letter in range(1,nr_letters+1):
    password_char.append(random.choice(letters))
for number in range(1,nr_numbers+1) :
    password_char.append(random.choice(numbers))
for symbol in range(1,nr_symbols+1):
    password_char.append(random.choice(symbols))

password1 = ''
random.shuffle(password_char)
for i in password_char:
    password1 += i

print(f'Here is the more strong password - {password1}')