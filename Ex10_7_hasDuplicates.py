#Author : Ishwar Jindal
#Created On : 07-Jul-2019 06:49 PM
#Purpose : Checks if a list has duplicate elements

def has_duplicates(lstItems):
    lstCopy = lstItems[:]
    lstCopy.sort()
    for index in range(0,len(lstCopy)-1):
        if lstCopy[index] == lstCopy[index+1]:
            return True
    return False

print("main started")
list1 = ["Ishwar","Amit","Jindal","Monika","Amit"]
list2 = ["0105","0103","0209","2703","2508","2107","0104","2512"]

if has_duplicates(list1):
    print (str.format("{0} has ***duplicates***", list1))
else:
    print (str.format("{0} doesn't have duplicates", list1))


if has_duplicates(list2):
    print (str.format("{0} has ***duplicates***", list2))
else:
    print (str.format("{0} doesn't have duplicates", list2))
    
print("main ended")
