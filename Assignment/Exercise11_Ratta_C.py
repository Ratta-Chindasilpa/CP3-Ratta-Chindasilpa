number = int(input("Enter: "))
for i in range(number):
    space = number - (i + 1)
    even = i +(i + 1)
    print(" " * space ,"*" * even)
