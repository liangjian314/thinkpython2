# 10_1编写一个叫做 nested_sum 的函数，接受一个由一些整数列表构成的列表作为参数，并将所有嵌套列表中的元素相加。
def nested_sum(t):
    for i in range(len(t)):
        if isinstance(t[i], list):
            t[i] = nested_sum(t[i])
    return sum(t)


print(nested_sum([[1, 2], [3], [4, 5, 6]]))

# 10_2编写一个叫做 cumsum 的函数，接受一个由数值组成的列表，并返回累加和； 即一个新列表，其中第i个元素是原列表中前i+1个元素的和。
def cumsum1(t):
    a = t[:]
    print(len(t))
    for i in range(len(t)):
        a[i] = sum(t[:i+1])
    return a


print(cumsum1([1, 2, 3]))

# 10_3编写一个叫做 middle 的函数，接受一个列表作为参数，并返回一个除了第一个和最后一个元素的列表。
def middle(t):
    return t[1:(len(t)-1)]


print(middle([1, 2, 3, 4]))
