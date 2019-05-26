#Author : Ishwar Jindal
#Created On : 26-May-2019 12:03 PM IST
#Purpose : Read a file and print word on screen having greater than N number of chars

print("main started")
fin = open("words.txt")
minimum_length = 20

for line in fin:
    word = line.strip()
    if len(word) > minimum_length:
        print(word)
print("main ended")
