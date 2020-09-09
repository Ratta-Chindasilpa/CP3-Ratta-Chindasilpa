'''x = int(input("Enter : "))
y = "*" * x
print(y)'''

'''number = int(input())
text = ""
for i in range(number):
    text = text + "*"
print(text)'''

'''number = int(input())
print(number * "*")'''

'''number = int(input("Enter: "))
for i in range(number):
    print(i)
    print("*" * (i+1))'''

number = int(input("Enter: "))
for x in range(number):
    text = ""
    for y in range(x + 1):
        text = text + "*"
    print(text)