# 编写一个叫作``ack ``的阿克曼函数来计算 Ackermann 函数，并使用你的函数计算 ack（3，4）
def ack(m, n):
    """m和n为非负整数"""
    if m == 0:
        return n+1
    if n == 0:
        return ack(m-1, 1)
    return ack(m-1, ack(m, n-1))


print(ack(3, 4))
