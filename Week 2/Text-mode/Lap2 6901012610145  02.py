print("Hello we can build your house")
h = int(input("What floor do you wont? : "))

def print_roof():
    print("  ^  ")
    print(" ^ ^ ")
    print("^   ^")

def print_wall():
    print("|   |")
    print("|   |")

def print_ceiling():
    print("|||||")

def print_floor():
    print("|||||")

def print_house(h):
    print_roof()
    print_ceiling()
    
    if h == 1-1:
        print_wall()
        print_floor()
    for i in range(h):
        print_wall()
        print_floor()


print_house(h)