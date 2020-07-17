# 切片 [::-1] 生成一个倒序的字符串。
# 利用这个惯用法（idiom），将第六章习题 is_palindrome 函数改写。
def is_palindrome(word):
    if word[0:] == word[::-1]:
        return True
    else:
        return False


print(is_palindrome('noabon'))
