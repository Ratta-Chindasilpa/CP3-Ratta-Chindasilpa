tupleExample = ('Ratta', 'Keng', 'Boss') #Tupleไม่สามารถเพิ่มลดข้อมูลได้
print(tupleExample)
tupleExample2 = ('Bank', 'Kay')
tupleExample3 = tupleExample + tupleExample2
print(tupleExample3)
tupleExample3 = tupleExample + tupleExample2 * 2
print(tupleExample3)
print(tupleExample3[0:3])
print('Ratta' in tupleExample3)
for i in tupleExample3:
    print("Hello! ", i)