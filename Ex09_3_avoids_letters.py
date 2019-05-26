#Author : Ishwar Jindal
#Created On : 26-May-2019 01:00 PM IST
#Purpose : Print words that avoids all characters passed in given string

def has_no_char(word, char_to_be_missing):
    for char in word:
        if char == char_to_be_missing:
            return False
    return True

def avoids(word, letters_to_avoid):
    for letter in letters_to_avoid:
        if has_no_char(word, letter) == True:
            continue
        else:
            return False;
    return True;

print("main started")
total = 0
matched = 0

letters_to_avoid = input("Enter letters that should be avoided in word : ")
fin = open("mywords.txt")
for line in fin:
    total = total + 1
    word = line.strip()
    if avoids(word, letters_to_avoid):
        matched = matched + 1
        print(str.format("{0} doesn't have any letter from {1}", word, letters_to_avoid))

print(str.format("{0} words out of {1} i.e. {2}% avoids {3}", matched, total, round(matched*100/total, 2), letters_to_avoid))

print("main ended")
