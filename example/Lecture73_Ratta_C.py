menuList = []
systemMenu ={'Pizza':20, 'Burger':25, 'Coke':15}
totalPrice = 0

def showBill():
    sayMyFood = "My Food"
    print(sayMyFood.center(50,"-"))
    for number in range(len(menuList)):
        print("Menu: ", menuList[number][0],"\tPrice: ",menuList[number][1])
    print("Total Price : ", totalPrice)

while True:
    menuName= input("Please Enter Menu : ")
    if(menuName.lower() == 'exit'):
        break
    else:
        menuList.append([menuName, systemMenu[menuName]])
        totalPrice = totalPrice + systemMenu[menuName]
print(menuList)

showBill()
