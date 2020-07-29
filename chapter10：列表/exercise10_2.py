# 10_7编写一个叫做 has_duplicates 的函数，接受一个列表作为参数， 如果一个元素在列表中出现了不止一次，则返回 True 。 这个函数不能改变原列表。
def has_duplicates(t):
    for i in t:
        if t.count(i) > 1:
            return True
        else:
            return False


print(has_duplicates([[1, 2], [1, 2], 3]))

# 10_8如果你的班级上有23个学生,2个学生生日相同的概率是多少？你可以通过随机产生23个生日，并检查匹配来估算概率。
# 提示：你可以使用random模块中的randint函数来生成随机生日。
import random
def randomBirthday():
    return str(random.randint(1, 12))+"-"+str(random.randint(1, 30))


def calculate():
    b = []
    for i in range(23):
        birthday = randomBirthday()
        print(birthday)
        b.append(birthday)
    # 生日相同的对数
    count = 0
    for i in range(len(b)):
        for j in range(len(b)-i-1):
            if b[i+j+1] == b[i]:
                count = count + 1

    return count / 23


print(calculate())
