def find(word, letter, index):
    while index < len(word):
        if word[index] == letter:
            return index
        index = index + 1
    return -1

def count(word, letter):
    found_at = find(word, letter, 0)
    letter_count = 0
    while found_at != -1:
        letter_count = letter_count + 1
        found_at = find(word, letter, found_at + 1)
    
    return letter_count

print ("main started")
word = "annnnnnnna"
letter = "a"
print ("The letter [" + letter + "] exist [" + str(count(word, letter)) + "] time(s) in [" + word + "]")

word_to_find = "nn"
print ("The letters [" + word_to_find + "] exist [" + str(word.count(word_to_find)) + "] time(s) in [" + word + "]")

print ("main ended")
