# love calculator

name1 = input("Enter your name: ")
name2 = input("Enter your crush name: ")

combined_names = name1 + name2
combined_lower = combined_names.lower()

t = combined_lower.count("t")
r = combined_lower.count("r")
u = combined_lower.count("u")
e = combined_lower.count("e")

true = t + r + u + e

l = combined_lower.count("l")
o = combined_lower.count("o")
v = combined_lower.count("v")
e = combined_lower.count("e")

love = l + o + v + e

love_score = str(true) + str(love)

score = int(love_score)

if (score < 10) or (score > 90):
    print(f"Your score is {love_score}, you go together like coke and mentos!")
elif (score >= 40) and (score <= 50):
    print(f"Your score is {love_score}, you are alright together")
else:
    print(f"Your score is {love_score}")

