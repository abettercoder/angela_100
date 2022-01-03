# Rock Paper Scisissors

import random

Rock = '''
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''
Paper = '''
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''
Scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

print("Welcome to Rock Paper Scissors!")
user_choice = input("Please choose one of the following: Type 0 for Rock, 1 for Paper or 2 for Scissors\n")

if user_choice == "0":
    print(Rock)
elif user_choice == "1":
    print(Paper)
elif user_choice == "2":
    print(Scissors)
else:
    print("Please enter a valid number")

computer_choice = random.randint(0, 2)
print(f"The computer has chosen: {computer_choice}")

if (user_choice == 0 and computer_choice == 0) or (user_choice == 1 and computer_choice == 1) or (user_choice == 2 and computer_choice == 2):
    print("It's a tie!")
elif (user_choice == 0 and computer_choice == 1) or (user_choice == 1 and computer_choice == 2) or (user_choice == 2 and computer_choice == 0):
    print("You lose!")
elif(user_choice >=3 or user_choice < 0):
    print("You lose, you have entered an invalid number")
else:
      print("You win!")