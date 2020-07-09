import turtle
import math

# 画n边形, 当n越大，画出的n边型趋近于圆


def polygon(t, length, n, angle=360):
    for i in range(n):
        t.fd(length)
        t.lt(angle/n)


# 使用海龟t画一个半径为r的圆
def circle(t, r):
    n = 600
    circumference = math.pi*2*r
    polygon(t, circumference/n, n)


def arc(t, r, angle):

    n = 600
    circumference = math.pi*2*r
    polygon(t, circumference/n, n, angle)


bob = turtle.Turtle()
arc(bob,  60, 180)
turtle.mainloop()
