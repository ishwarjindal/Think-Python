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
    print (str.format("Invocation count : {0}", pass_count + 1))
    if len(list_of_words) == 0:
        return False;

    if len(list_of_words) == 1:
        return list_of_words[0] == word_to_find

    target_index = -1
    lower_index = -1
    upper_index = -1
    
    if len(list_of_words) % 2 == 0:
        target_index = int(len(list_of_words) / 2)
    else:
        target_index = int(((len(list_of_words) + 1) / 2) - 1)

    if list_of_words[target_index] == word_to_find:
        return True
    elif list_of_words[target_index] > word_to_find:
        lower_index = 0
        upper_index = target_index - 1
    else:
        lower_index = target_index + 1
        upper_index = len(list_of_words) - 1

    if lower_index > upper_index:
        return False
    else:
        return in_bisect(list_of_words[lower_index:upper_index+1], word_to_find, pass_count + 1)

    
print("main started")

list_of_words = build_list_using_append()
word_to_find = "loopside"
pass_count = 0

if in_bisect(list_of_words, word_to_find, pass_count) == True:
    print(str.format("{0} is in list", word_to_find))
else:
    print(str.format("{0} is not in list", word_to_find))
    
print("main ended")
