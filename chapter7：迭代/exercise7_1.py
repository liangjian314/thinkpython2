# 复制平方根一节中的循环，将其封装进一个叫 mysqrt 的函数中。
# 这个函数接受 a 作为形参，选择一个合适的 x 值，并返回 a 的平方根估算值。


def mysqrt(a):
    x = 3
    epsilon = 0.00000000001
    i = 0
    while True:
        i = i+1
        y = (x+a/x)/2
        if abs(y-x) < epsilon:
            break
        x = y
    print("数字"+str(a)+"的平方根是"+str(y)+", 计算了"+str(i)+"次")
    return y


print(mysqrt(100))
