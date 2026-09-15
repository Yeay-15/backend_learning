weight = int(input("Enter your weight (kg): "))
height = int(input("Enter your height (cm): "))

bmi = round(weight((height/10**2)),2)

print(f"your weight is", weight)
print(f"your height is", height)
      
print(f"your bmi is", bmi)

if bmi < 18.5:
    print("You are underweight")
elif bmi <= 25:
    print("You Are normal")
elif bmi <= 30:
    print("You are  overweight")
elif bmi <= 40:
    print("You are obese")
else:
    print("You are extremely obese")
