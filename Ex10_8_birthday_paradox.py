#Author : Ishwar Jindal
#Created On : 11-Jul-2019 07:45 PM IST
#Purpose : Find probability of same birthday in a group of 23 people

import random

def has_duplicates(lstItems):
    lstCopy = lstItems[:]
    lstCopy.sort()
    for index in range(0,len(lstCopy)-1):
        if lstCopy[index] == lstCopy[index+1]:
            return True
    return False

def get_random_birthdays(num_of_birthdays):

    birthday_list = []
    
    for index in range(0, num_of_birthdays):

        random_month = random.randint(1,12)

        if random_month in [1,3,5,7,8,10,12]:
            random_day = random.randint(1,31)
        elif random_month in [4,6,9,11]:
            random_day = random.randint(1,30)
        else:
            random_day = random.randint(1,29)

        birthday_list.append(str(random_day).zfill(2)+str(random_month).zfill(2))
    return birthday_list


print("main started")

sample_size = 100
number_of_students = 23
duplicates_found = 0

for index in range(0, sample_size):
    list_of_birthdays = get_random_birthdays(number_of_students)
    if sample_size <= 10:
        print(list_of_birthdays)
    if has_duplicates(list_of_birthdays):
        duplicates_found += 1

print(str.format("In sample size of {0}, {1} has duplicate birthdays which is {2}%",sample_size, duplicates_found,int((duplicates_found*100)/sample_size)))

print("main ended")
