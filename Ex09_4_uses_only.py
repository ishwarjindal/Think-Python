#Author : Ishwar Jindal
#Created On : 26-May-2019 05:19 PM IST
#Purpose : Find words that uses only the specificed letters

def has_no_char(word, char_to_be_missing):
    for char in word:
        if char == char_to_be_missing:
            return False
    return True

def uses_only(word, letters_to_use):
    for letter in word:
        if has_no_char(letters_to_use, letter) == False:
            continue
        else:
            return False
    return True

print("main started")
total = 0
matched = 0

letters_to_use = input("Enter the superset of letters to be used in word : ")
fin = open("words.txt")
for line in fin:
    total = total + 1
    word = line.strip()
    if uses_only(word, letters_to_use):
        matched = matched + 1
        print(str.format("{0} does have all letters in {1}", word, letters_to_use))

print(str.format("{0} words out of {1} i.e. {2}% have all their letters in {3}", matched, total, round(matched*100/total, 2), letters_to_use))

print("main ended")
