from tkinter import *

root = Tk()  # create parent window

def equals(ans):
    match op[-1]:
        case 1:
            ans.set(n[-2] + n[-1])
        case 2:
            ans.set(n[-2] - n[-1])
        case 3:
            ans.set(n[-2] * n[-1])
        case 4:
            ans.set(n[-2] / n[-1])

ans = IntVar()
n = []
op = []

# use Button and Label widgets to create a simple TV remote
no9 = Button(root, text="9", command=lambda : n.append(9))
no9.grid(column=0, row=0)

no8 = Button(root, text="8", command=lambda : n.append(8))
no8.grid(column=1, row=0)

no7 = Button(root, text="7", command=lambda : n.append(7))
no7.grid(column=2, row=0)

no6 = Button(root, text="6", command=lambda : n.append(6))
no6.grid(column=0, row=1)

no5 = Button(root, text="5", command=lambda : n.append(5))
no5.grid(column=1, row=1)

no4 = Button(root, text="4", command=lambda : n.append(4))
no4.grid(column=2, row=1)

no3 = Button(root, text="3", command=lambda : n.append(3))
no3.grid(column=0, row=2)

no2 = Button(root, text="2", command=lambda : n.append(2))
no2.grid(column=1, row=2)

no1 = Button(root, text="1", command=lambda : n.append(1))
no1.grid(column=2, row=2)

plus = Button(root, text="+", command=lambda : op.append(1))
plus.grid(column=3, row=0)

minus = Button(root, text="-", command=lambda : op.append(2))
minus.grid(column=3, row=1)

times = Button(root, text="x", command=lambda : op.append(3))
times.grid(column=3, row=2)

divide = Button(root, text="/", command=lambda : op.append(4))
divide.grid(column=3, row=3)

equal = Button(root, text="=", command=lambda: equals(ans))
equal.grid(column=2, row=3)

answer = Label(root, textvariable=ans)
answer.grid(column=0, row=3)

root.mainloop()
