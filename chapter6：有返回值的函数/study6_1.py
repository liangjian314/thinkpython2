# 返回给定半径的圆的面积
import math


# def area(radius):
#     return math.pi*radius**2


# print(area(5))


# 写一个比较函数，接受两个值 x 和 y 。 如果 x > y， 则返回 1 ；如果 x == y， 则返回 0 ；如果 x < y，则返回 -1
def compare(x, y):
    if x > y:
        return 1
    if x == y:
        return 0
    if x < y:
        return -1


print(compare(-2, -1))


# 计算两个给定坐标点 (x_1,y_1) 和 (x_2, y_2) 之间的距离。根据勾股定理（the Pythagorean theorem），二者的距离是：

# distance = sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2}

# def distance(x1, y1, x2, y2):
#     a1 = x2-x1
#     b1 = y2-y1
#     value1 = a1**2+b1**2
#     return(math.sqrt(value1))


# print(distance(1, 2, 4, 6))


# 运用增量开发方式，写一个叫作 hypotenuse 的函数，接受直角三角形的两直角边长作为实参，返回该三角形斜边的长度。记录下你开发过程中的每一步

def hypotenuse(a, b):
    z = a**2+b**2
    return(math.sqrt(z))


print(hypotenuse(3, 4))


# 知道圆心和圆周上一点的横纵坐标，计算圆的面积

def distance(x1, y1, x2, y2):
    a1 = x2-x1
    b1 = y2-y1
    value1 = a1**2+b1**2
    return(math.sqrt(value1))  # 计算半径


def area(radius):
    return math.pi*radius**2  # 计算面积


def circle_area(xc, yc, xp, yp):
    return area(distance(xc, yc, xp, yp))  # 封装


print(circle_area(1, 2, 4, 6))


# 写一个函数 is_between(x, y, z) ，如果x<=y<=z 返回 True 否则返回 False。


def is_between(x, y, z):
    if x <= y <= z:
        return True
    else:
        return False


print(is_between(0, -2, 1))


# 计算阶乘


def factorial(n):
    if not isinstance(n, int):
        print('小数无阶乘。')
        return None
    elif n < 0:
        print('负数无阶乘。')
        return None
    elif n == 0:
        return 1
    else:
        recurse = factorial(n-1)
        return n*factorial(n-1)


print(factorial(5))
