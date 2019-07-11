#Author : Ishwar Jindal
#Created On : 07-Jul-2019 12:29 PM
#Purpose : Return cumulatve sum of the list of numbers

def cumsum(lstNumbers):
    lstCumSum = []
    for index in range(0, len(lstNumbers)):
        lstCumSum.append(sum(lstNumbers[0:index+1]))
    return lstCumSum

print("main started")
lstNums = [1,2,4,6,7,9,10]
print(str.format("The cumulative sum of {0} is {1}",lstNums, cumsum(lstNums)))
print("main ended")
