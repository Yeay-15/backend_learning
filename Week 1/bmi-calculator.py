print("Welcome to the BMI Calculator Program")

data_validation = False
while data_validation != True:
    weight = input("Enter your weight (kg): ")
    height = input("Enter your height (cm): ")
    try:
        weight = float(weight)
        height = float(height)
        data_validation = True
    except ValueError:
        print("Invalid number. Please input numeric values")
        continue

    bmi = round(weight/((height/100)**2), 2)

    print(f"your weight is {weight}")
    print(f"your height is {height}")      
    print(f"your bmi is {bmi}")

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
