#Author : Ishwar Jindal
#Created On : 07-Jul-2019 12:55 PM
#Purpose : Check if two words are anagram

def is_anagram(word1, word2):
    if len(word1) != len(word2):
        return False
    
    list1 = list(word1.upper())
    list2 = list(word2.upper())

    list1.sort()
    list2.sort()
    
    for index in range(0, len(list1)):
        if list1[index] != list2[index]:
            return False
    return True

print("main started")
w1 = "Ishwar"
w2 = "rashiw"

if is_anagram(w1,w2):
    print(str.format("{0} and {1} are anagram", w1,w2))
else:
    print(str.format("{0} and {1} are not anagram", w1,w2))

w1 = "noon"
w2 = "oonn"

if is_anagram(w1,w2):
    print(str.format("{0} and {1} are anagram", w1,w2))
else:
    print(str.format("{0} and {1} are not anagram", w1,w2))


w1 = "marg"
w2 = "grams"

if is_anagram(w1,w2):
    print(str.format("{0} and {1} are anagram", w1,w2))
else:
    print(str.format("{0} and {1} are not anagram", w1,w2))


w1 = "Dehydration"
w2 = "radietondhy"

if is_anagram(w1,w2):
    print(str.format("{0} and {1} are anagram", w1,w2))
else:
    print(str.format("{0} and {1} are not anagram", w1,w2))

    
print("main ended")
