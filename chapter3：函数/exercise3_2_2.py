# zhaodong
def do_twice(f):
    f()
    f()


def do_three(f):
    f()
    f()
    f()


def do_four(f):
    do_twice(f)
    do_twice(f)


def print_1():
    print("+----", end="")

def print_2():
    print("|    |    |    |")


def grid():
    do_three(print_1)
    print("+")
    do_four(print_2)
    do_three(print_1)
    print("+")
    do_four(print_2)
    do_three(print_1)
    print("+")
    do_four(print_2)
    do_three(print_1)
    print("+")
