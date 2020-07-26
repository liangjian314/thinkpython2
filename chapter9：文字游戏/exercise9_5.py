# 编写一个名为uses_all的函数，接受一个单词和一个必须使用的字符组成的字符串。
# 如果该单词包括此字符串中的全部字符至少一次，则返回True。
def uses_all(word, uses_str):
    for letter in uses_str:
        if letter not in word:
            return False
    return True


print(uses_all('hell', 'hello'))
