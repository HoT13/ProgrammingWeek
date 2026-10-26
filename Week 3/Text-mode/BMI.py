weight = float(input("Enter your weight in kg: "))
height = int(input("Enter your height in cm: "))/100

def calculate_bmi(weight, height):
    bmi = weight / (height  2)
    return bmi

def bmi_category_adult(bmi):
    if bmi < 18.5:
        print("Underweight")
    elif 18.5 <= bmi < 25:
        print("Normal weight")
    elif 25 <= bmi < 30:
        print("Overweight")
    elif 30 <= bmi < 35:
        print("Obesity class 1")
    elif 35 <= bmi < 40:
        print("Obesity class 2")
    else:
        print("Obesity class 3")

bmi = calculate_bmi(weight, height)
print(f"Your BMI is: {bmi:.2f}")
bmi_category_adult(bmi)