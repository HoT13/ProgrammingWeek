width = float(input("Enter the width of the rectangle(meters): "))
length = float(input("Enter the length of the rectangle(meters): "))
area = width * length
print(f"The area of the rectangle is: {area} square meters")

sports_fields = {"football": 7140,"basketball": 400,"tennis/volleyball": 162}

def check_sports_field(area,value):
    if area >= value:
        return True
    return False

for sport, value in sports_fields.items():
    if check_sports_field(area,value):
        print(f"The area is adequate for a {sport} field.")
    else:
        print(f"The area is not adequate for a {sport} field.")