def find_rounds(numbers:list):
    # collect the number from list in order from small to large
    # Each round goes through the list from left to right and collects a number 
    # if it is the next number to be collected. 
    # 
    # The process ends when all numbers have been collected.
    all_subsets=[]
    rounds_count = 0
    
    # get the smallest element
    new_numbers= numbers
    while len(new_numbers) >0 :
        small_num, index = (numbers[0],0)
        sub_set = []
        # get the small num
        for i in range(len(new_numbers)):
            
            if new_numbers[i] < small_num:
                small_num = new_numbers[i]
                index = new_numbers.index(small_num)
        sub_set.append(small_num)
        # new_numbers.remove(small_num)
        # numbers_length = len(new_numbers)
        ind = index
        while ind < len(new_numbers):
            
            if new_numbers[ind] == small_num +1 :
                sub_set.append(new_numbers[ind])
                small_num = new_numbers[ind]
                
                
            else:
                ind += 1
        all_subsets.append(sub_set)
        rounds_count +=1
        for ss in sub_set:
            new_numbers.remove(ss)
        
        
                
                
        # new_numbers.remove(small_num)
    return all_subsets, rounds_count




if __name__ == "__main__":
    print(find_rounds([1, 2, 3, 4]))
    # [[1, 2, 3, 4]]

    print(find_rounds([1, 3, 2, 4]))
    # [[1, 2], [3, 4]]    

    print(find_rounds([4, 3, 2, 1]))
    # [[1], [2], [3], [4]]
    
    print(find_rounds([1]))
    # [[1]]

    print(find_rounds([2, 1, 4, 7, 5, 3, 6, 8]))
    # [[1], [2, 3], [4, 5, 6], [7, 8]]