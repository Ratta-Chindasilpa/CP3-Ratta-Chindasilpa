'''
if True:
    print("Hello welcome!")
    if True:
        print("Yo! Mister A")
        if True:
            print("HaHa")
'''

usernameInput = input("Username: ")
passwordInput = input("Password: ")
if usernameInput == "Ratta" and passwordInput == "1150":
    print("Done!")
    print("---- iShop ----")
    print("1. Vat Calculator")
    print("2. Price Calculator")
    userSelected = int(input("Enter your demand: "))
    if userSelected == 1:
        price = int(input("Price (THB) : "))
        vat = 7
        result = price +(price * vat / 100)
        print(result)
    elif userSelected == 2:
        price1 = int(input("First Product Price : "))
        price2 = int(input("Second Product Price : "))
        print(price1 + price2)
