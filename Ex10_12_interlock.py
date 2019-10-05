#Author : Ishwar Jindal
#Created On : 05-Oct-2019 07:01 PM IST
#Purpose : Find words which interlock

def getWordList():
    file = open("words.txt")
    wordList = []
    for word in file:
        wordList.append(word.strip())

    return wordList;

def in_bisect(list_of_words, word_to_find):
    number_of_words = len(list_of_words)
   
    if number_of_words == 0 or len(word_to_find) == 0:
        return False

    if number_of_words == 1:
        return list_of_words[0] == word_to_find

    list_middle = number_of_words//2

    if  word_to_find == list_of_words[list_middle]:
        return True
    elif word_to_find > list_of_words[list_middle]:
        return in_bisect(list_of_words[list_middle + 1:], word_to_find)
    else:
        return in_bisect(list_of_words[:list_middle-1], word_to_find)

            
def isInterlock(wordListToCheck, wordToCheck):
    firstWord = wordToCheck[::2]
    secondWord = wordToCheck[1::2]
    return in_bisect(wordListToCheck, firstWord) and in_bisect(wordListToCheck, secondWord)

def isInterlock(wordListToCheck, wordToCheck, n):
    for counter in range(n):
        partialWord = word[counter::n]
        if not in_bisect(wordListToCheck, partialWord):
            return False
    return True

if __name__ == "__main__":        
    print("main started")
    wordList = getWordList()
    wordListCopy = wordList[:]
    for word in wordList:
        if isInterlock(wordListCopy, word, 3):
            print(str.format("{0} : is 3-way interlock of {1}, {2} and {3}", word, word[::3], word[1::3], word[2::3]))
    print("main ended")
