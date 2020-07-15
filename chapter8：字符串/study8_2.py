# 遍历一个序列并在找到寻找的东西时返回,被称作搜索。
# 遍历一个字符串并找到某字符在该字符串中的索引。
def find(word, letter):
    index = 0
    while index < len(word):
        if word[index] == letter:
            return index
        index = index+1
    return -1


print(find('China', 'C'))

# 修改 ``find``函数使得它接受第三个参数，即从何处开始搜索的索引。


def find(word, letter, n):
    while n < len(word):
        if word[n] == letter:
            return n
        n = n+1
    return -1


print(find('China', 'a', 1))

# 计算字母a在字符串中出现的次数。
word = 'banana'
count = 0
for letter in word:
    if letter == 'a':
        count = count+1
print(count)

# 将这段代码封装在一个名为 count 的函数中，
# 并泛化该函数，使其接受字符串和字母作为实参。


def count(word, letter):
    count1 = 0
    for i in word:
        if i == letter:
            count1 = count1+1
    print(count1)


count('banana', 'b')

# 重写这个函数，不再使用字符串遍历，
# 而是使用上一节中三参数版本的 find 函数。
def count1(word, letter):
    count = 0
    i = 0
    while i < len(word):
        index = find(word, letter, i)
        if index==-1:
            break
        else:
            count = count+1
            i = index+1
    return count

print(count1("banana","w"))
