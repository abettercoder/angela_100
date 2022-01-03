print("Welcome to the tip calculator")

bill = float(input("What was the total bill ?\n"))
tip_percent = float(input("What percentage tip would you like to give ?\n"))
people_to_split = int(input("How many people to split the bill ?\n"))

total_bill = bill/people_to_split
tip = bill/people_to_split * (tip_percent/100)

total_pay_per_person = round(total_bill + tip,2)
print(f"Each person should pay: {total_pay_per_person}")