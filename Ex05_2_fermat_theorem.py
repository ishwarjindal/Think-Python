def check_fermat(a,b,c,n):
    lhs = a**n + b**n
    rhs = c**n
    if (lhs == rhs and n > 2):
        print('Holy smokes, Fermat was wrong!')
    else:
        print('No, that doesn\'t work')
        

a = input('Enter a : ')
b = input('Enter b : ')
c = input('Enter c : ')
n = input('Enter n : ')

check_fermat(int(a), int(b), int(c), int(n))

    
