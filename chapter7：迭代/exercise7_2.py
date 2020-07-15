# 内置函数 eval 接受一个字符串，并使用 Python 解释器来计算该字符串。
# 编写一个名为 eval_loop 的函数，迭代式地提示用户输入，获取输入的内容，并利用 eval 来计算其值，最后打印该值。
# 该程序应持续运行，直到用户输入 'done'，然后返回它最后一次计算的表达式的值。
def eval_loop():
    while True:
        line = input('')
        if line == 'done':
            break
        print(line)
        return eval(line)


print(eval_loop())
