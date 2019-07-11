#Author : Ishwar Jindal
#Created On : 06-Jul-2019 04:15 PM
#Purpose : Calculate sum of intergers of all nested lists in a give list

def nested_sum(listOfNumbers):
    sum_total = 0
    for listItem in listOfNumbers:
        sum_total += sum(listItem)

    return sum_total

print("main started")
lst = [[1,2,3],[4,5],[6],[7,8],[9,10,11,12,13,14,15]]
sum_total = nested_sum(lst)
print (str.format("sum of all elements of {0} is {1}",lst, sum_total))
print("main ended")
