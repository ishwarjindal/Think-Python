#Author : Ishwar Jindal
#Created On : 26-May-2019 12:14 PM IST
#Purpose : Read a file and print word on screen having no "e" in it

def has_no_char(word, char_to_be_missing):
    for char in word:
        if char == char_to_be_missing:
            return False
    return True


print("main started")
fin = open("words.txt")
missing_char = "e"
total_words = 0
mathcing_words = 0

for line in fin:
    total_words = total_words + 1
    word = line.strip()
    if has_no_char(word, missing_char):
        mathcing_words = mathcing_words + 1
        print(word)

print(str.format("{0} words out of {1} i.e. {2}% of the word are missing {2} character", total_words, mathcing_words, round(mathcing_words*100/total_words, 2), missing_char))
print("main ended")
