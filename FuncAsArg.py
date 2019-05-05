# script to test passing function as argument

def print_spam(arg1):
    print(arg1)

def do_twice(f, arg1):
    f(arg1)
    f(arg1)
def do_four(f, arg1):
    do_twice(f, arg1)
    do_twice(f, arg1)
    
do_four(print_spam,"Py for Python")
    
