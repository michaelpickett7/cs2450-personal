from random import randint
print("Hello, I'm going to guess your age. ")
name = input("What is your name? ")
while (True):
    guess = randint(15,40)
    print(f"Are you {guess} years old? ")
    answer = input()
    if (answer == "y"):
        print(f"{name} is {guess} years old.")
        exit(0)
    else:
        print("Rats")
