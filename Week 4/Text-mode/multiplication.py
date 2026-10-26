def multiplication_table(n):
    for i in range(1, 13):
        print(f"{n} x {i} = {n * i}")

number = int(input("Enter a number: "))
multiplication_table(number)