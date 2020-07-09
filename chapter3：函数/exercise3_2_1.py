def grid1():
    print('+'+'-'*4+'+'+'-'*4+'+')
def grid2():
    print('|'+' '*4+'|'+' '*4+'|')
def do_twice():
    grid2()
    grid2()
def do_four():
    do_twice()
    do_twice()
def grid():
    grid1()
    do_four()
    grid1()
    do_four()
    grid1()
