# 接受一个函数对象和一个数n作为实参， 能够调用指定的函数n次
# def do_n(s, n):
#     if n <= 0:
#         return
#     s()
#     do_n(s, n-1)

# def pring_1():
#     print("1")

# do_n(pring_1,7)

def do_n(s, n):
    if n <= 0:
        return
    print(s)
    do_n(s, n-1)


do_n(input('name:'), int(input('number:')))


