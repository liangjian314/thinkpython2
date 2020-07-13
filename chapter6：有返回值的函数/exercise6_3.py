# 当数字 a 能被 b 整除，并且 a/b 是 b 的幂时， 它就是 b 的幂。
# 编写一个叫 is_power 的函数，接受两个参数 a 和 b， 并且当 a 是 b 的幂时返回 True。注意：你必须要想好基础情形。
def is_power(a, b):
    if a == b:
        return True
    if a % b == 0 and is_power(a/b, b):
        return True
    else:
        return False


a = 16
b = 2
print(str(a)+'是'+str(b)+"的幂? "+str(is_power(a, b)))
