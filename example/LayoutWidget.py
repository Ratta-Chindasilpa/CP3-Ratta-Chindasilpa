from tkinter import *

def sayHelloWorld():
    print("Hello World!!")

MainWindow = Tk()
button1 = Button(MainWindow,text = "Click Me1", command = sayHelloWorld).grid(row=0,column=0)
#button.place(x=50,y=20)
button2 = Button(MainWindow,text = "Click Me2", command = sayHelloWorld).grid(row=1,column=1)
#button2.place(x=125,y=20)
button3 = Button(MainWindow,text = "Click Me3", command = sayHelloWorld).grid(row=2,column=2)
MainWindow.mainloop()