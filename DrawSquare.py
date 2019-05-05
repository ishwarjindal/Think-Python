# print square
def printdashedline(n):
    print("+"+"-"*n+"+"+"-"*n+"+")

def printemptyline(n):
    print("|"+" "*n+"|"+" "*n+"|")

def draw_box(line1f, line2f, spacing):
    line1f(spacing)
    line2f(spacing)
    line2f(spacing)
    line2f(spacing)
    line2f(spacing)
    line1f(spacing)
    line2f(spacing)
    line2f(spacing)
    line2f(spacing)
    line2f(spacing)
    line1f(spacing)

draw_box(printdashedline, printemptyline, 10)
