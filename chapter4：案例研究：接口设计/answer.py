# 1.写一个名为 square 的函数，接受一个名为 t 的形参，t 是一个海龟。
# 这个函数应用这只海龟画一个正方形。
# 写一个函数调用，将 bob 作为实参传给 square ，然后再重新运行程序。
import turtle
import math


# def square(t):
#     for i in range(4):
#         t.fd(100)
#         t.lt(90)


# bob = turtle.Turtle()
# square(bob)


# 2.给 square 增加另一个名为 length 的形参。
# 修改函数体，使得正方形边的长度是 length ，然后修改函数调用，提供第二个实参。
# 重新运行程序。用一系列 length 值测试你的程序。
# def square(t, length):
#     for i in range(4):
#         t.fd(length)
#         t.lt(90)


# bob = turtle.Turtle()
# square(bob,100)
# 3.复制 square ，并将函数改名为 polygon 。
# 增加另外一个名为 n 的形参并修改函数体，
# 让它画一个正n边形（n-sided regular polygon）。
# 提示：正n边形的外角是360/n度。
# def polygon(t, length, n, angle=360):
#     for i in range(n):
#         t.fd(length)
#         t.lt(angle/n)


# polygon(bob, 100, 7)
# 4.编写一个名为 circle 的函数，它接受一个海龟t和半径r作为形参，
# 然后以合适的边长和边数调用 polygon ，画一个近似圆形。 用一系列r值测试你的函数。
# 提示：算出圆的周长，并确保 length * n = circumference 。


# def circle(t, r):
#     circumference = 2*math.pi*r
#     n = 50
#     length = circumference/n
#     polygon(t, length, n)


# bob = turtle.Turtle()
# circle(bob, 30)
# 5.完成一个更泛化（general）的 circle 函数，称其为 arc ，
# 接受一个额外的参数 angle ，确定画多完整的圆。
# angle 的单位是度，因此当 angle=360 时， arc 应该画一个完整的圆。
def polygon(t, length, n, angle=360):
    for i in range(n):
        t.fd(length)
        t.lt(angle/n)

def arc(t, r, angel):
    circumference = 2*math.pi*r
    n = 50
    length = circumference/n
    polygon(t, length, n, angel)


bob = turtle.Turtle()
arc(bob, 30, 160)
