text = "Hello"
print(text[0], text[1], text[2], text[3], text[4])
print(text[0] + "Hello")
print(text[:-1])
print(text[0:4])

address = "642/17 Sukhumvit Bangkok"
print("Sukhumvit" in address)
print("Bangkok" not in address)

name = "Ratta"
weight = "100"
print("Hello " + name + "! and weight is " + weight +"kg")
print("Hello %s! and weight is %skg" % (name, weight))
# %d = จำนวนเต็ม, %f = ทศนิยม, %s = ข้อความ