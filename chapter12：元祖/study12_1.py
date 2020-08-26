# 编写一个叫做 small 的函数，使它能够接受任何数量的实参并返回它们的和。
def small(*lis):
    return sum(lis)


n = 1, 2, 3, 4, 5
p = 1, 2, 3
o = 10
m = [1, 2]
print(small(*n, *p, o, *m))
