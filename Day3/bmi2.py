height = float(input("Enter your height in m: "))
weight = float(input("Enter your weight in m: "))

bmi = round(weight/ (height**2),2)

if bmi<18.5 :
    print(f"Your bmi is {bmi}, You are underweight.")
elif (25>bmi>18.5):
    print(f"Your bmi is {bmi}, You have normal weight.")
elif (30>bmi>25):
    print(f"Your bmi is {bmi}, You are overweight.")
elif (30>bmi>35):
    print(f"Your bmi is {bmi}, You are obese.")
else :
    print(f"Your bmi is {bmi}, You are clinically obese.")
