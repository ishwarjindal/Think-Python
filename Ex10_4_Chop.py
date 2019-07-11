#Author : Ishwar Jindal
#Created On : 07-Jul-2019 12:37 PM
#Purpose : Chop the list

def chop(lst):
    #lst1 = lst[:]
    lst.pop(0)
    lst.pop(-1)
    return None

print("main started")
myList = [10,20,30,40,50]
print(str.format("List before chopping is {0}", myList))
chop(myList)
print(str.format("List after chopping is {0}", myList))
print("main ended")
