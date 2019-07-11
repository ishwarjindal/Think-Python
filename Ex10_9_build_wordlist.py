#Author :Ishwar Jindal
#Created On : 11-Jul-2019 08:39 PM IST
#Purpose : See if append is faster or + []

import time

def build_list_using_append():
    file = open("words.txt")
    lst = []
    for word in file:
        lst.append(word)
    print(len(lst))

def build_list_using_addition():
    file = open("words.txt")
    lst = []
    for word in file:
        lst = lst + [word]
    print(len(lst))

print("main started")
print("Append")
localtime = time.asctime( time.localtime(time.time()) )
print(str.format("Start Time : {0}", localtime))

build_list_using_append()

localtime = time.asctime( time.localtime(time.time()) )
print(str.format("End   Time : {0}", localtime))

print("Addition")
localtime = time.asctime( time.localtime(time.time()) )
print(str.format("Start Time : {0}", localtime))

build_list_using_addition()

localtime = time.asctime( time.localtime(time.time()) )
print(str.format("End   Time : {0}", localtime))

print("main ended")
