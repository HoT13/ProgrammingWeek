score = float(input("Enter your score: "))

def grade_category(score):
    if score >= 80:
        return "A"
    elif score >= 70:
        return "B"
    elif score >= 60:
        return "C"
    elif score >= 50:
        return "D"
    else:
        return "F"

x = grade_category(score)
print(f"Your grade is: {x}")