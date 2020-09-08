usernameInput = input("Username: ")
passwordInput = input("Password: ")
if usernameInput == "Ratta" and passwordInput == "1150":
    print("----- Welcome in!! -----")
    print("1.Banana : 5 THB/piece")
    print("2.Orange : 10 THB/piece")
    print("3.Apple  : 15 THB/piece")
    userSelected = int(input("Enter your demand: "))
    banana_price = 5
    orange_price = 10
    Apple_price = 15
    if userSelected == 1:
        bananaQuatities = int(input(("Enter your banana quatities: ")))
        print("Your demand: Banana, ", bananaQuatities, "piece(s)")
        total_banana = banana_price * bananaQuatities
        print("Total payment: ", total_banana, "(THB)")
    elif userSelected == 2:
        orangeQuatities = int(input(("Enter your orange quatities: ")))
        print("Your demand: Orange, ", orangeQuatities, "piece(s)")
        total_orange = orange_price * orangeQuatities
        print("Total payment: ", total_orange, "(THB)")
    elif userSelected == 3:
        appleQuatities = int(input(("Enter your apple quatities: ")))
        print("Your demand: Orange, ", appleQuatities, "piece(s)")
        total_apple = apple_price * appleQuatities
        print("Total payment: ", total_apple, "(THB)")

elif usernameInput == "Ratta" and passwordInput != "1150":
    print("Wrong password!")
else:
    print("Error!")