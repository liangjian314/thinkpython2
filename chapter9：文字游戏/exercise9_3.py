# 编写一个名为 avoids 的函数，接受一个单词和一个指定禁止使用字符的字符串，
# 如果单词中不包含任意被禁止的字符，则返回True 。
def avoids(word, avoid_str):
    for letter in word:
        if letter in avoid_str:
            return False
    return True


print(avoids('banana', 'abcdefg'))
