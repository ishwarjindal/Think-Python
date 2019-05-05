def do_twice(f,s):
    f(s)
    f(s)

def print_spam(s):
    print(s)

def do_four(f,s):
    do_twice(f,s)
    do_twice(f,s)


do_four(print_spam,"spam")
