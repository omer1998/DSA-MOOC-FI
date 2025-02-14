def count_sublists(numbers):
    
#     last_element = 0
#     sublist_length = 0
#     count = 0 

#     for i in range(len(numbers)):
#         if i == 0 or numbers[i] > numbers[i-1]:
#             sublist_length+=1
#         else:
#             sublist_length= 1
#         count += sublist_length

#     return count
    



            
        



    count_length = 0
    count = 0

    for i in range(len(numbers)):
        if i == 0 or  numbers[i] <= numbers[i-1]:
            count_length = 1
        else:
            count_length +=1
        count += count_length
    

    return count

    

if __name__ == "__main__":
    print(count_sublists([2, 1, 3, 4])) # 7
    print(count_sublists([1, 2, 3, 4])) # 10
    print(count_sublists([4, 3, 2, 1])) # 4
    print(count_sublists([1, 1, 1, 1])) # 4
    print(count_sublists([1, 2, 1, 2])) # 6

    # numbers = list(range(1, 10**5+1))
    # print(count_sublists(numbers)) # 5000050000