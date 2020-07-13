# 当n的值大于0，打印出n的值，然后让n减1。当n递减至0时，打印单词Blastoff！”。
def countdown(n):
    while n > 0:
        print(n)
        n = n-1
    print('Blastoff!')


print(countdown(2))

# 利用迭代而非递归，重写print_n函数
# def countdown(n):
#     if n <= 0:
#         print('Blastoff!')
#     else:
#         print(n)
#         countdown(n-1)


def print_n(s, n):
    while n > 0:
        print(s)
        n = n-1
    return


print(print_n(3, 5))
