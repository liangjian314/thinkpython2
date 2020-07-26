# 编写一个名为uses_only的函数，接受一个单词和一个字符串。
# 如果该单词只包括此字符串中的字符，则返回True。
def uses_only(word, uses_str):
    for letter in word:
        if letter not in uses_str:
            return False
    return True


print(uses_only('acefh', 'acefhlo'))
