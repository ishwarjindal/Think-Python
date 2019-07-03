#Author : Ishwar Jindal
#Created On : 26-May-2019 08:06 PM IST
#Purpose : Find words having letters in alphabatical order

def is_abecedarian(word):
    last_ord = 0
    for char in word:
        if ord(char) >= last_ord:
            last_ord = ord(char)
            continue
        else:
            return False
    return True

print("main started")
total = 0
matched = 0

fin = open("words.txt")
for line in fin:
    total = total + 1
    word = line.strip()
    if is_abecedarian(word):
        matched = matched + 1
        print(str.format("{0} has letters in alphabatical order",word))

print(str.format("{0} out of {1} i.e. {2}% words are in alphabatical order",matched, total, round(matched*100/total,2)))
print("main ended")
