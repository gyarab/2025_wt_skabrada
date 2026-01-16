import math
from turtle import forward, left, right, exitonclick


def stena(a):
    forward(a)
    left(90)
    forward(a)
    left(90)
    forward(a)
    left(90)
    forward(a)
    left(90)

def kolmiceAstrecha(a):
    left(45)
    forward(math.sqrt(a**2 + a**2))
    right(135)
    forward(a)
    right(135)
    forward(math.sqrt(a**2 + a**2))
    right(90)
    forward(math.sqrt(a**2 + a**2) / 2)
    right(90)
    forward(math.sqrt(a**2 + a**2) / 2)
def backToStart(a):
    right(45)
    forward(a)
    left(90)

def domecek():
    stena(30)
    kolmiceAstrecha(30)
    backToStart(30)

for i in range(36):
    domecek()
    right(10)



exitonclick()