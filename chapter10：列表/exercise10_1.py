# 10_1编写一个叫做 nested_sum 的函数，接受一个由一些整数列表构成的列表作为参数，并将所有嵌套列表中的元素相加。
def nested_sum(t):
    for i in range(len(t)):
        if isinstance(t[i], list):
            t[i] = nested_sum(t[i])
    return sum(t)


print(nested_sum([[1, 2], [3], [4, 5, 6]]))

# 10_2编写一个叫做 cumsum 的函数，接受一个由数值组成的列表，并返回累加和； 即一个新列表，其中第i个元素是原列表中前i+1个元素的和。


def cumsum(t):
    a = t[:]
    print(len(t))
    for i in range(len(t)):
        a[i] = sum(t[:i+1])
    return a


print(cumsum([1, 2, 3]))

# 10_3编写一个叫做 middle 的函数，接受一个列表作为参数，并返回一个除了第一个和最后一个元素的列表。


def middle(t):
    return t[1:(len(t)-1)]


print(middle([1, 2, 3, 4]))

# 10_4编写一个叫做 chop 的函数，接受一个列表作为参数，移除第一个和最后一个元素，并返回None。


def chop(t):
    del t[0]
    del t[-1]
    print(t)
    return None


print(chop([1, 2, 3, 4]))

# 10_5编写一个叫做``is_sorted``的函数，接受一个列表作为参数， 如果列表是递增排列的则返回 True ，否则返回False。


def is_sorted(t):
    a = t[:]
    a.sort()
    if t == a:
        return True
    else:
        return False


print(is_sorted([1, 3, 2, 4]))

# 10_6如果可以通过重排一个单词中字母的顺序，得到另外一个单词，那么称这两个单词是变位词。
# 编写一个叫做 is_anagram 的函数，接受两个字符串作为参数， 如果它们是变位词则返回 True 。


def is_anagram(str_one, str_two):
    a = list(str_one)
    b = list(str_two)
    a.sort()
    b.sort()
    if a == b:
        return True
    else:
        return False


print(is_anagram('abc', 'bca'))


    