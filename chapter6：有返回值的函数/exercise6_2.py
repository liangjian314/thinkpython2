# 回文词（palindrome）指的是正着拼反着拼都一样的单词，如 “noon”和“redivider”。 按照递归定义的话，如果某个词的首字母和尾字母相同，而且中间部分也是一个回文词，那它就是一个回文词
# 编写一个叫 is_palindrome 的函数，接受一个字符串作为实参。如果是回文词，就返回 True ，反之则返回 False。记住，你可以使用内建函数 len 来检查字符串的长度。
def first(word):
    return word[0]


def last(word):
    return word[-1]


def middle(word):
    return word[1:-1]


def is_palindrome(word):
    if len(word) <= 1:
        return True
    if first(word) != last(word):
        return False
    return is_palindrome(middle(word))


print(is_palindrome('noon'))
