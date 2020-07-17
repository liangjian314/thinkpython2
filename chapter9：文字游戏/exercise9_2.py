# 9_2_1写一个叫做has_no_e的函数，如果给定的单词中不包含字符“e”，其返回 True 。
fin = open('./chapter9：文字游戏/words.txt')
for line in fin:
    word = line.strip()


def has_no_e(word):
    for letter in word:
        if letter == 'e':
            return False
    return True


print(has_no_e(word))

# 9_2_2修改上一节中的程序，只打印不包含“e”的单词，并且计算列表中不含“e”单词的比例。
def ratio_e():
    fin = open('./chapter9：文字游戏/words.txt')
    count = 0
    not_e_count = 0
    for line in fin:
        word = line.strip()
        count = count+1
        if has_no_e(word) == True:
            not_e_count = not_e_count+1
            print(word)
    return not_e_count/count


print(ratio_e())



