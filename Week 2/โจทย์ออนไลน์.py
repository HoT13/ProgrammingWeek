def convert_temp(celsius):
    fahrenheit = (celsius * 9/5) + 32  
    print("Result: " + str(fahrenheit) + " F")

c = float(input("Enter temperature in Celsius: "))
convert_temp(c)