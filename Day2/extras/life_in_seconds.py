age = input("What is your current age ?\n")
age = int(age)

# If you will live for 90 years

years_rem = 90 - age
days_rem = years_rem * 365
weeks_rem = years_rem * 52
months_rem = years_rem * 12

seconds_rem = days_rem * 24 * 60 * 60

life_rem_sec = print(f"you have {seconds_rem} seconds remaining.")

print(life_rem_sec)
