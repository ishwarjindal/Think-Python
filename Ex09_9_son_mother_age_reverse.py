#Author : Ishwar Jindal
#Created On : 01-Jun-2019 04:29 PM IST
#Purpose : Find the age of son where in last 6 instance his age and his mother age were opposite in number including current age and 2 instance in future have same pattern

print("main started")


son_age = 7
age_instance_found = 0

while True:     #loop #1
    #print(str.format("Looping for son's age of {0}", son_age))
    mother_age = int(str(son_age).zfill(2)[::-1])
    if mother_age > son_age:
        #print(str.format("Looping for mother's age of {0}", mother_age))
        age_instance_found = 1
        print(str.format("Match #{2} Found in past: Son {0}, Mother {1}", son_age, mother_age, age_instance_found))
    
        for boy_past_age in range(son_age-1, 1, -1):    #loop #2
            #print(str.format("Looping for son's past age of {0}", boy_past_age))
            mother_age = mother_age - 1
        
            if str(boy_past_age).zfill(2)[::-1] == str(mother_age):
                age_instance_found = age_instance_found + 1
                print(str.format("Match #{2} Found in past: Son {0}, Mother {1}", boy_past_age, mother_age, age_instance_found))

            if age_instance_found == 6:
                mother_age = int(str(son_age).zfill(2)[::-1]) + 1
                
                for boy_future_age in range(son_age + 1, 1000 , 1):   #loop #3
                    if str(boy_future_age).zfill(2)[::-1] == str(mother_age):
                        age_instance_found = age_instance_found + 1
                        print(str.format("Match #{2} Found in future: Son {0}, Mother {1}", boy_future_age, mother_age, age_instance_found))

                    if age_instance_found == 8:
                        print(str.format("*******Current age of son is {0}", son_age))
                        break               #come out of loop #3
                    else:
                        mother_age = mother_age + 1 #contiue loop #3
            else:
                continue    #continue loop #2
                    
            if age_instance_found == 8:
                break #come out of loop #2
            else:
                continue#continue loop #2
            
    if age_instance_found == 8:
        break    #come out of loop #1
    else:
        son_age = son_age + 1
    
print("main ended")
