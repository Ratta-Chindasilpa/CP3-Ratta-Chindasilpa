fruits = {'apple', 'banana','pineapple', 'orange'}
print(fruits)
#fruits.clear()
fruits.remove('banana')
print(fruits)

userInput = int(input("Enter Number of Your Favorite Fruits : "))
myFruits = set()
while(len(myFruits) < userInput):
    myFruits.add(input("Fruits : "))
    print(myFruits)

'''a = [1,2,3,4,5,4,3,2,1]
b = set(a)
print(b)'''

'''b = {"d","b","d","d","o","f","g","a"}
print(b)'''
