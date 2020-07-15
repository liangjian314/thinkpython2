# while倒序打印字符
def search_show(text):
    i = len(text)-1
    while i >= 0:
        print(text[i])
        i = i - 1

# for倒序打印字符
def search_show_for1(text):
    for i in range(len(text)):
        j = len(text)-i
        print(text[j-1])


# while正序打印字符
def search_show2(text):
    i = 0
    while i < len(text):
        print(text[i])
        i = i+1

# for正序打印字符


def search_show_for2(text):
    for i in text:
        print(i)


search_show_for1('abcd')
