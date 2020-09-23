#https://www.w3schools.com/js/js_json_arrays.asp
#JSON จะเป็นข้อมูลที่มีรูปแบบคล้ายกับ list ใน python ที่เก็บข้อมูลแบบ key value
'''{
    "name": "John",
    "age": 30,
    "cars": ["Ford", "BMW", "Fiat"]
}'''

import json

#Read JSON
def readJson():
    # ข้อมูล JSON ที่เราต้องการอ่าน
    x =  '{ "name":"John", "age":30, "city":"New York"}'
    # แปลงข้อมูลให้กลายเป็นรูปที่เราสามารถใช้ได้
    y = json.loads(x)
    # ทำการเรียกข้อมูล name ออกมาแสดง
    print(y["name"])

readJson()

#Convert Python to JSON
def writeJson():
    # สร้างข้อมูลที่เราต้องการแปลง(ประเภท dictionary)
    x = {
        "name": "John",
        "age": 30,
        "city": "New York"
    }
    # คำสั่งที่ใช้ในการแปลง
    y = json.dumps(x)
    # มาลองดูผลลัพธ์กัน
    print(y)

writeJson()


