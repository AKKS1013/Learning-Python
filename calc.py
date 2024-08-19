from tkinter import *

root = Tk()  # create parent window

def plus():
    ans = a + b
    print(ans)

def minus():
    ans = a - b
    print(ans)

def times():
    ans = a * b
    print(ans)

def divide():
    ans = a / b
    print(ans)

ans = 0
a = 0
b = 0

# use Button and Label widgets to create a simple TV remote
no9 = Button(root, text="9", command=(a:=9))
no9.grid(column=0, row=0)

no8 = Button(root, text="8", command=(a:=8))
no8.grid(column=1, row=0)

no7 = Button(root, text="7", command=(a:=7))
no7.grid(column=2, row=0)

no6 = Button(root, text="6", command=(a:=6))
no6.grid(column=0, row=1)

no5 = Button(root, text="5", command=(a:=5))
no5.grid(column=1, row=1)

no4 = Button(root, text="4", command=(a:=4))
no4.grid(column=2, row=1)

no3 = Button(root, text="3", command=(a:=3))
no3.grid(column=0, row=2)

no2 = Button(root, text="2", command=(a:=2))
no2.grid(column=1, row=2)

no1 = Button(root, text="1", command=(a:=1))
no1.grid(column=2, row=2)

plus = Button(root, text="+", command=plus)
plus.grid(column=3, row=0)

minus = Button(root, text="-", command=minus)
minus.grid(column=3, row=1)

times = Button(root, text="x", command=times)
times.grid(column=3, row=2)

divide = Button(root, text="/", command=divide)
divide.grid(column=3, row=3)

root.mainloop()
