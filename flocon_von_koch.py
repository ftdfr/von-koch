import turtle
from tkinter import *

init = 1
t = turtle.Turtle()
l = 0
n = 0


def triangle():
    t.clear()
    t.pencolor("black")
    t.penup()
    t.goto(-100, 100)
    t.pendown()
    t.speed(1)
    for i in range(3):
        t.forward(300)
        t.left(240)

    
def koch1():
    def init():
        t.clear()
        t.pencolor("black")
        t.penup()
        t.goto(-100, 100)
        t.pendown()
        t.speed(1)

    def koch(l, n):
        if n <= 0:
            t.forward(l)
        else:
            koch(l / 3, n - 1)
            t.left(60)
            koch(l / 3, n - 1)
            t.right(120)
            koch(l / 3, n - 1)
            t.left(60)
            koch(l / 3, n - 1)

    def flocon(l, n):
        init()
        koch(l, n)
        t.right(120)
        koch(l, n)
        t.right(120)
        koch(l, n)
    flocon(300, 1)

def koch2():
    def init():
        t.clear()
        t.pencolor("black")
        t.penup()
        t.goto(-100, -100)
        t.pendown()
        t.speed(0)

    def koch(l, n):
        if n <= 0:
            t.forward(l)
        else:
            koch(l / 3, n - 1)
            t.left(60)
            koch(l / 3, n - 1)
            t.right(120)
            koch(l / 3, n - 1)
            t.left(60)
            koch(l / 3, n - 1)

    def flocon(l, n):
        init()
        koch(l, n)
        t.right(120)
        koch(l, n)
        t.right(120)
        koch(l, n)
    flocon(300, 2)


def koch3():
    def init():
        t.clear()
        t.pencolor("black")
        t.penup()
        t.goto(0, 0)
        t.pendown()
        t.speed(0)

    def koch(l, n):
        if n <= 0:
            t.forward(l)
        else:
            koch(l / 3, n - 1)
            t.left(60)
            koch(l / 3, n - 1)
            t.right(120)
            koch(l / 3, n - 1)
            t.left(60)
            koch(l / 3, n - 1)

    def flocon(l, n):
        init()
        koch(l, n)
        t.right(120)
        koch(l, n)
        t.right(120)
        koch(l, n)
    flocon(300, 3)


def koch4():
    def init():
        t.clear()
        t.pencolor("black")
        t.penup()
        t.goto(-100, -50)
        t.pendown()
        t.speed(0)

    def koch(l, n):
        if n <= 0:
            t.forward(l)
        else:
            koch(l / 3, n - 1)
            t.left(60)
            koch(l / 3, n - 1)
            t.right(120)
            koch(l / 3, n - 1)
            t.left(60)
            koch(l / 3, n - 1)

    def flocon(l, n):
        init()
        koch(l, n)
        t.right(120)
        koch(l, n)
        t.right(120)
        koch(l, n)
    flocon(300, 4)


window = Tk()
window.geometry("225x150")
window.title("Koch")
button_level0 = Button(window, text="Triangle", command=triangle)
button_level1 = Button(window, text="1", command=koch1)
button_level2 = Button(window, text="2", command=koch2)
button_level3 = Button(window, text="3", command=koch3)
button_level4 = Button(window, text="4", command=koch4)
button_level0.pack()
button_level1.pack()
button_level2.pack()
button_level3.pack()
button_level4.pack()

window.mainloop()