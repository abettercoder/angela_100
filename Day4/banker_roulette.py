import random

names_string = input("Enter names separated by commas: ")
names_list = names_string.split(",")

list_length = len(names_list)

roulette = random.randint(0, list_length - 1)
print("Bill will be paid by : " + names_list[roulette])