print("Hello, I'm going to guess your age. ")
name = input("What is your name? ")
while (True) {
    guess = random(15,40)
    printf("Are you {guess} years old? ")
    answer = input()
    if (answer == "y") {
        printf("{name} is {guess} years old.")
        exit
    }
    else {
        print("Rats")
    }
}
