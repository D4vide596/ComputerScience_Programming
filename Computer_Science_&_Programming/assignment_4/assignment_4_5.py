if __name__ == "__main__":

    #ask variable
    height = float(input("Enter your height (cm): "))
    weight = float(input("Enter your weight (kg): "))

    #calculate BMI
    bmi = (weight / (height**2)) * 10000

    print(f"Your BMI is: {bmi:.2f}")

    #say the correct answers
    if bmi < 18.5:
        print("You are in a Underweight range!")
    elif 18.5 <= bmi < 25:
        print("You are in a Healthy weight range!")
    elif 25 <= bmi < 30:
        print("You are in a Overweight range!")
    elif bmi >= 30:
        print("You are in a Obese range")