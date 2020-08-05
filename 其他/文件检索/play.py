def find_keyword():
    file = open('.\其他\文件检索\log.log')
    keys = ['question4', 'question1', 'exception']
    for (num, keyword) in enumerate(file):
        for word in keys:
            if keyword.find(word) != -1:
                print(num, keyword)


find_keyword()
