from tkinter import *

screen = Tk()
screen.geometry('320x240')
screen.title('ATM')

a = 1000

def clear():
    for widget in screen.winfo_children():
        widget.destroy()

def dep():
    global D
    clear()
    lblD = Label(screen, text="Deposit: ")
    lblDD = Label(screen, text="$")
    D = Entry(screen)

    lblD.grid(row=0, column=0)
    D.grid(row=0, column=1)
    lblDD.grid(row=0, column=2)

    btn = Button(screen, text="OK", command=sumd)
    btn.grid(row=1, column=0, columnspan=2)

    ee = D.get()
    print(ee)

def sumd():
    global D
    global a

    b = D.get()
    a += int(b)
    print(a)
    info2()


def wit():
    global ew
    clear()
    lblW = Label(screen, text="Withdraw: ")
    lblWW = Label(screen, text="$")
    ew = Entry(screen)

    lblW.grid(row=0, column=0)
    ew.grid(row=0, column=1)
    lblWW.grid(row=0, column=2)

    btnW = Button(screen, text="OK", command=subw)
    btnW.grid(row=1, column=0, columnspan=2)

    ee = ew.get()
    print(ee)

def subw():
    global ew
    global a

    b = ew.get()
    a -= int(b)
    print(a)
    info2()


def bal():
    clear()
    global a
    lblB = Label(screen, text="The balance is: " +str(a) + "$")
    lblB.grid(row=0, column=0)
    btnB = Button(screen, text="Exit", command= info2)
    btnB.grid(row=1, column=0, columnspan=2)

def ex():
    screen.destroy()


def info2():
    print("OK!")
    clear()
    btnD = Button(screen, text = "Deposit", command = dep)
    btnD.grid(row=0, column=0, columnspan=2)

    btnW = Button(screen, text = "Withdraw", command = wit)
    btnW.grid(row=1, column=0, columnspan=2)

    btnB = Button(screen, text = "Balance", command = bal)
    btnB.grid(row=2, column=0, columnspan=2)

    btnE = Button(screen, text= "Exit" , command = ex)
    btnE.grid(row=3, column=0, columnspan=2)

def info():
    global p
    if p.get() == "1":
        print("OK")
        clear()
        btnD = Button(screen, text = "Deposit", command = dep)
        btnD.grid(row=0, column=0, columnspan=2)

        btnW = Button(screen, text = "Withdraw", command = wit)
        btnW.grid(row=1, column=0, columnspan=2)

        btnB = Button(screen, text = "Balance", command = bal)
        btnB.grid(row=2, column=0, columnspan=2)

        btnE = Button(screen, text= "Exit" , command = ex)
        btnE.grid(row=3, column=0, columnspan=2)

def screenone():
    global p
    lbl = Label(screen, text = "Login")
    lbl.grid(row=0, column=0, columnspan = 2)

    Password = Label(screen, text = "Password")
    p = Entry(screen)

    Password.grid(row= 1, column=0)
    p.grid(row=1, column=1)

    btn = Button(screen, text = "Submit", command = info)
    btn.grid(row=2, column=0, columnspan = 2)

screenone()
screen.mainloop()

