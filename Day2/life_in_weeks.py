age = input("What is your current age ?\n")
age = int(age)

# If you will live for 90 years

years_rem = 90 - age
days_rem = years_rem * 365
weeks_rem = years_rem * 52
months_rem = years_rem * 12

life_rem = print(f"you have {days_rem} days, {weeks_rem} weeks and {months_rem} months")

print(life_rem)