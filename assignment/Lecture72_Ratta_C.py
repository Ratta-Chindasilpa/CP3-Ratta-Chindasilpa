menuList = []
priceList = []
#temp = [[10,10],[20,10]] # List อยู่ใน Listได้
#print(temp[0:2])
totalPrice = 0

def showBill():
    sayMyFood = "My Food"
    print(sayMyFood.center(50,"-"))
    for number in range(len(menuList)):
        print("Menu : ", menuList[number][0],"\nPrice : ",menuList[number][1])
    print("Total Price : ", totalPrice)

while True:
    menuName = input("Please Enter Menu : ")
    if(menuName.lower() == 'exit'):
        break
    else:
        menuPrice = int(input("Price : "))
        totalPrice = totalPrice + menuPrice
        menuList.append([menuName, menuPrice])
        #menuList.append(menuPrice)
        #priceList.append(menuPrice)
print(menuList)
#print(menuList, priceList)

showBill()