'''
inputRound = int(input("Please Enter Number : "))
print(list(range(inputRound)))
sum = 0
for x in range(inputRound):
    print(x)
    inputNumber = int(input("x" + str(x+1) + " :"))
    sum = sum + inputNumber
print("Result : " ,sum)
'''

start = int(input("Start: "))
step = int(input("Step: "))
result = str()
for i in range(5):
    print(i)
    print(start + step * i, end = " ")
    #result += str(start + step * i +1)
    #print(result)
