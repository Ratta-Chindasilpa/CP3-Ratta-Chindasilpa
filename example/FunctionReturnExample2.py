'''usernameInput = input("Username: ")
passwordInput = input("Password: ")
if usernameInput == "admin" and passwordInput == "1234":
    print("Done !")
    print("----- iShop -----")
    print("1. Vat Calcualtor")
    print("2. Price Calculator")
    userSelected = int(input(">>"))
    if userSelected == 1:
        price = int(input("Price (THB) : "))
        vat = 7
        result = price +(price * vat / 100)
        print(result)
    elif userSelected == 2:
        price1 = int(input("First Product Price: "))
        price2 = int(input("Second Product Price: "))
        print(price1 + price2)'''
#Login
#Show Menu
#Select Menu
#Vat
#Price

def login():
    usernameInput = input("Username: ")
    passwordInput = input("Password: ")
    if usernameInput == "admin" and passwordInput == "1234":
        return True
    else:
        return False
def showMenu():
    print("----- iShop -----")
    print("1. Vat Calcualtor")
    print("2. Price Calculator")
def menuSelect():
    userSelected = int(input(">>"))
    return userSelected
def vatCalculate(totalPrice):
    vat = 7
    result = totalPrice + (totalPrice * vat / 100)
    return result
def priceCalculate():
    price1 = int(input("First Product Price: "))
    price2 = int(input("Second Product Price: "))
    return vatCalculate(price1 + price2)

print(priceCalculate())