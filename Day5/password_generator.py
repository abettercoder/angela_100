# password generator
import random
letters = "a b c d e f g h i j k l m n o p q r s t u v w x y z"
numbers = "0 1 2 3 4 5 6 7 8 9"
symbols = "! @ # $ % ^ & * ( ) _ +"

letter = letters.split(" ")
number = numbers.split(" ")
symbol = symbols.split(" ")

print("Welcome to the password generator!")

nr_of_letters = int(input("How many letters do you want in your password? \n"))
nr_of_numbers = int(input("How many numbers do you want in your password? \n"))
nr_of_symbols = int(input("How many symbols do you want in your password? \n"))

# Easy Level
password = ""
for char in range(1, nr_of_letters + 1):
    password += random.choice(letter)
for nr in range(1, nr_of_numbers + 1):
    password += random.choice(number)
for sym in range(1, nr_of_symbols + 1):
    password += random.choice(symbol)
print(password)

# Hard Level
# passwordlist = []
#for char in range(1,nr_of_letters+1):
#    password_list += random.choice(letter)
#    for nr in range(1,nr_of_numbers+1):
#        password_list += random.choice(number)
#        for symb in range(1,nr_of_symbols+1):
#            password_list += random.choice(symbol)
#random.shuffle(password_list)
#print(password_list)

#password_hard = ""
#for char in password_list:
#    password_hard += char
#print(f"Your password is {password_hard}")

