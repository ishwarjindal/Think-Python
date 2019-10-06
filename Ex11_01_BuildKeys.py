#Author : Ishwar Jindal
#Created On : 06-Oct-2019 07:48 AM IST
#Purpose : Find word in list of words using dictionary

def getWordList():
    file = open('words.txt')
    words = dict()
    for word in file:
        words[word.strip()]=''
    return words

if __name__ == "__main__":
    print("main started")
    wordsList = getWordList()
    print(str.format("Dictionary has {0} word", len(wordsList)))

    wordToFind = "naked"
    if wordToFind in wordsList:
        print(str.format("{0} is in list",wordToFind))
    else:
        print(str.format("{0} is not in list",wordToFind))
        
    print("main ended")
