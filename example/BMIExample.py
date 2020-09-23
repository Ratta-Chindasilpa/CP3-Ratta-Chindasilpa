from tkinter import *
import math

def leftClickButton(event):
    BMI = float(textBoxWeight.get()) / math.pow(float(textBoxHeight.get())/100, 2)
    if BMI > 30.0:
        BMIResult = 'อ้วนมาก'
    elif BMI >= 25.0:
        BMIResult = 'อ้วน'
    elif BMI >= 23.0:
        BMIResult = 'น้ำหนักเกิน'
    elif BMI >= 18.6:
        BMIResult = 'น้ำหนักปกติ เหมาะสม'
    elif BMI < 18.5:
        BMIResult = 'ผอมเกินไป'

    print(textBoxHeight.get(), textBoxWeight.get()) # .getดึงค่าข้อมูลจากEntry
    #print(float(textBoxWeight.get()) / math.pow(float(textBoxHeight.get())/100, 2))
    labelResult.configure(text=BMIResult)
    # .configure คือการกำหนดค่า

MainWindow = Tk()
lableHeight = Label(MainWindow, text ="ส่วนสูง (cm.)")
lableHeight.grid(row=0,column=0)
textBoxHeight = Entry(MainWindow) #กล่องใส่ค่า
textBoxHeight.grid(row=0,column=1)

lableWeight = Label(MainWindow, text ="น้ำหนัก (kg.)")
lableWeight.grid(row=1,column=0)
textBoxWeight = Entry(MainWindow) #กล่องใส่ค่า
textBoxWeight.grid(row=1,column=1)

calculationButton = Button(MainWindow, text = "คำนวณ")
calculationButton.grid(row=2, column=0)
calculationButton.bind('<Button-1>', leftClickButton)

labelResult = Label(MainWindow,text="ผลลัพธ์")
labelResult.grid(row=2,column=1)
MainWindow.mainloop()
