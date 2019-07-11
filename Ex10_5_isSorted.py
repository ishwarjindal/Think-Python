#Author : Ishwar Jindal
#Created On : 07-Jul-2019 12:43 PM
#Purpose : Check if list is sorted or not

def is_sorted(lst):
    
    if len(lst) == 1:
        return True

    for index in range(1,len(lst)):
        if ord(str(lst[index])) < ord(str(lst[index-1])):
            return False
    return True

print("main started")
myList1 = [1,2,3,4,5,6,7]
myList2 = ['a','b','c','d','f','e','z']
myList3 = ['A','B','D','C']

print(str.format("List {0} is sorted={1}", myList1, is_sorted(myList1)))
print(str.format("List {0} is sorted={1}", myList2, is_sorted(myList2)))
print(str.format("List {0} is sorted={1}", myList3, is_sorted(myList3)))
print("main ended")
