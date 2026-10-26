choice = int(input("put your number here"))

def say_hello(choice):
    if choice == 1:
        print("Hello KMUTNB")
    elif choice == 2:
        print("Sawasdee KMUTNB")
    elif choice == 3:
        print ("Hallo, KMUTNB")
    elif choice == 4:
        print ("Error: there is no choice 4, please tryagain")
    else :
        print("Error there is no choicetry please try again ")

say_hello(choice)