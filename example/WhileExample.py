#start = 0
#while start <= 20:
#    print("I love you.")
#    start += 1

correctNumber = 17
userGuess = 0
while userGuess != correctNumber:
    userGuess = int(input("Please guess a number : "))
    if userGuess > correctNumber:
        print("Too Large")
    elif userGuess < correctNumber:
        print("Too Small")
    elif correctNumber == correctNumber:
        print("Correct!!")

