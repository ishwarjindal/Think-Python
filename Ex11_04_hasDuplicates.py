#Author : Ishwar Jindal
#Created On : 06-Oct-2019 09:07 AM
#Purpose : Checks if a list has duplicate elements

def has_duplicates(lstItems):
    items_dict = dict()
    for item in lstItems:
        if not item in items_dict:
            items_dict[item] = ''
        else:
            return True

    return False

if __name__ == "__main__":
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
