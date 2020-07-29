# 计算一个字符串中每个字母出现的次数。提示：字典类有一个 get 方法，接受一个键和一个默认值作为参数。
def histogram(s):
    d = dict()
    for c in s:
        d[c] = d.get(c, 0)+1
    return d


print(histogram('banana'))
