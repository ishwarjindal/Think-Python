#Author : Ishwar Jindal
#Created On : 26-May-2019 06:32 PM IST
#Purpose : Find words that uses all the specificed letters

def has_no_char(word, char_to_be_missing):
    for char in word:
        if char == char_to_be_missing:
            return False
    return True

def uses_all(word, letters_to_use):
    for letter in letters_to_use:
        if has_no_char(word, letter) == False:
            continue
        else:
            return False
    return True

print("main started")
matched = 0
total = 0

letters_to_use = input("Enter the letters to be used in word : ")

fin = open("words.txt")
for line in fin:
    total = total + 1
    word = line.strip()
    if uses_all(word, letters_to_use):
        matched = matched + 1
        print(str.format("{0} uses all letters from {1}", word, letters_to_use))

print(str.format("{0} out of {1} i.e. {2}% word uses all letters from {3}", matched, total, round(matched*100/total,2), letters_to_use))
print("main ended")
