#Author : Ishwar Jindal
#Created On : 06-Oct-2019 08:15 AM IST
#Purpose : Print frequencies of letters in sentence and vice versa

def getFrequenciesOfLetters(sentence):
    dict_letters = dict()
    for letter in sentence:
        dict_letters[letter] = dict_letters.setdefault(letter,0) + 1

    return dict_letters

def invert_dict(inputDict):
    inverted_dict = dict()
    for key in inputDict:
        inverted_dict.setdefault(inputDict[key],[]).append(key)

    return inverted_dict

if __name__ == "__main__":
    print("main started")
    sentence_1 = "the quick brown fox jumps over a little lazy dog"
    hist = getFrequenciesOfLetters(sentence_1)
    print(hist)
    
    inverted_hist = invert_dict(hist)
    print(inverted_hist)
    print("main ended")

