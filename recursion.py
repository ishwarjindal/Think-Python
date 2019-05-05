def print_1():
    print("N")
    

def do_n(f,n):
    if n <=0:
        return
    f()
    do_n(f, n-1)

do_n(print_1, 5)
