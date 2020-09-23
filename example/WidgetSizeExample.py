from tkinter import *

def sayHelloWorld():
    print("Hello World!!")

MainWindow = Tk()
button1 = Button(MainWindow,text = "Click Me1", command = sayHelloWorld, width=20, height=20).grid(row=0,column=0)
button2 = Button(MainWindow,text = "Click Me2", command = sayHelloWorld).grid(row=1,column=1)
button3 = Button(MainWindow,text = "Click Me3", command = sayHelloWorld).grid(row=2,column=2)
lable = Label(MainWindow, text ="What's up!!", width=20).grid(row=0,column=1)
MainWindow.mainloop()
