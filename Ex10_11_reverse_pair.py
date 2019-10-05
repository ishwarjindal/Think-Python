#Author : Ishwar Jindal
#Created On : 05-Oct-2019 01:58 PM IST
#Purpose : Find all reverse pairs in the word list

def getWordList():
    file = open("words.txt")
    wordList = []
    for word in file:
        wordList.append(word.strip())

    return wordList;

def in_bisect(list_of_words, word_to_find):
    number_of_words = len(list_of_words)
   
    if number_of_words == 0:
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

            
def findAndPrintReversePairs(wordList):
    print(str.format("got list with {0} elements", len(wordList)))
    wordListCopy = wordList.copy()

    for word in wordList:
        reversedWord = word[::-1]
        if in_bisect(wordListCopy, reversedWord):
            print(str.format("{0} is a reverse word", word))

if __name__ == "__main__":        
    print("main started")
    wordList = getWordList()
    findAndPrintReversePairs(wordList)
    print("main ended")
