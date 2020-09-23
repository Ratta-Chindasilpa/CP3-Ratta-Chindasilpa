#https://tkdocs.com/tutorial/widgets.html
#GUI = Graphic Main User Interface
from tkinter import *

def sayHelloWorld():
    print("Hello World!!")

MainWindow = Tk()
button1 = Button(MainWindow,text = "Click Me", command = sayHelloWorld)
button1.place(x=50,y=50)
MainWindow.mainloop()

MainWindow2 = Tk()
button2 = Button(MainWindow2,text = "Click Me", command = sayHelloWorld)
button2.place(x=1,y=1)
MainWindow2.mainloop()
