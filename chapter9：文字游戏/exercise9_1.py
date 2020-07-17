# 9_0读取并打印words.txt中的每个单词
fin = open('./chapter9：文字游戏/words.txt')
for line in fin:
    word = line.strip()
    print(word)

# 9_1编程写一个程序，使得它可以读取 words.txt　，然后只打印出那些长度超过20个字符的单词(不包括空格)。
fin = open('./chapter9：文字游戏/words.txt')
for line in fin:
    word = line.strip()
    if len(word)>20:
        print(word)

