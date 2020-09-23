#x = 'hello'
x = 'goodbye'

assert x == 'goodbye', "x should be 'hello'"  #ถ้าเงื่อนไขถูกต้อง(เป็นTrue) จะไม่Error

#assert i < 5, "Error"
for i in range(10):
    #assert i < 5, "Error"
    print(i)
    assert i < 5, "Error"