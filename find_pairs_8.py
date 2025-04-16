#Given two lsits 
list1 = [1,2,3,9]
list2 = [1,2,4,4] 
list3 = [1,2,3,4,5,6,7,8,9]

#find a pair of numbers that equal 8 

def find_8(given_list):
    pair_found = False
    i = 0
    j = 0 
    while i <= len(given_list) -1: 
        while j <= len(given_list) -1: 
            if given_list[i] + given_list[j] == 8 and i != j:
                #this will print the pairs found print(given_list[i],"and", given_list[j],"Makes 8!")
                j+=1
                pair_found = True
                continue
            else: 
                j+=1 
                continue 
        i+=1 
        j=0
        continue
    if pair_found == False: 
        print("no pairs found")
    else: 
        print("pair found")

find_8(list1)
find_8(list2)
find_8(list2)


