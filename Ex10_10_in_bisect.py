#Author : Ishwar Jindal
#Created On : 11-Jul-2019 09:24 PM IST
#Purpose : Find word in list using bisect method

def build_list_using_append():
    file = open("words.txt")
    lst = []
    for word in file:
        lst.append(word.strip())
        
    return lst
    
def in_bisect(list_of_words, word_to_find, pass_count):
    number_of_words = len(list_of_words)
 
    print (str.format("Invocation count : {0}, Item count : {1}", pass_count + 1, number_of_words))
   
    if number_of_words == 0:
        return False

    if number_of_words == 1:
        return list_of_words[0] == word_to_find

    list_middle = number_of_words//2

    if  word_to_find == list_of_words[list_middle]:
        return True
    elif word_to_find > list_of_words[list_middle]:
        return in_bisect(list_of_words[list_middle + 1:], word_to_find, pass_count + 1)
    else:
        return in_bisect(list_of_words[:list_middle-1], word_to_find, pass_count + 1)
    
print("main started")

list_of_words = build_list_using_append()
word_to_find = "naked"
pass_count = 0

if in_bisect(list_of_words, word_to_find, pass_count) == True:
    print(str.format("{0} is in list", word_to_find))
else:
    print(str.format("{0} is not in list", word_to_find))
    
print("main ended")
