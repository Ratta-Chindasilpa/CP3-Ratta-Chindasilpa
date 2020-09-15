menuList = []
priceList = []
totalPrice = 0

def showBill():
    sayMyFood = "My Food"
    print(sayMyFood.center(50,"-"))
    for number in range(len(menuList)):
        print(menuList[number], priceList[number])
        priceList[number] = priceList[number] + priceList[number]
    print("Total Price : ", totalPrice)

while True:
    menuName = input("Please Enter Menu : ")
    if(menuName.lower() == 'exit'):
        break
    else:
        menuPrice = int(input("Price : "))
        totalPrice = totalPrice + menuPrice
        menuList.append(menuName)
        #menuList.append(menuPrice)
        priceList.append(menuPrice)
#print(menuList)
print(menuList, priceList)

showBill()
