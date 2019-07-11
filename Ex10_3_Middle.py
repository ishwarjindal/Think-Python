#Author : Ishwar Jindal
#Created On : 06-Jul-19 04:24 PM
#Purpose : Return list of middle elements from list

def middle(listOfItems):
    return listOfItems[1:len(listOfItems)-1]

print("main started")
lst = ['a','b','c','d','e','f','g']
print(str.format("middle list of {0} is {1}", lst, middle(lst)))
print("main ended")
