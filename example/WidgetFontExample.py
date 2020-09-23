from tkinter import *

def sayHelloWorld():
    print("Hello World!!")

main = Tk()
text1 = Label(main, text ="What's up!!", width=20, fg='red', bg='blue', font=('Helvetica',76), anchor=W).grid(row=0,column=1)
text2 = Label(main, text ="Ratta!!", width=20, fg='pink', bg='purple', font=('Helvetica',76), anchor=E).grid(row=1,column=1)
main.mainloop()