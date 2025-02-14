
def find_rounds(numbers: list):

    remaining_nums = numbers[:]
    first_small_num = min(remaining_nums)
    small_num = first_small_num
    first_small_num_index= remaining_nums.index(small_num)

    all_sub_sets = []
    index = 0
    while remaining_nums:
        sub_set =[]
        if remaining_nums[index] == first_small_num:
            sub_set.append(first_small_num)
            remaining_nums.remove(first_small_num)
            for num in remaining_nums[first_small_num_index:]:
                if num == small_num+1:
                    sub_set.append(num)
                    remaining_nums.remove(num)
                    small_num +=1
            all_sub_sets.append(sub_set)
            first_small_num = small_num +1
            small_num = first_small_num
            first_small_num_index = index
            index= 0

                
        else:
            index +=1
            
    # all_sub_sets.append(sub_set)

    return all_sub_sets, len(all_sub_sets)
        
    


if __name__ == "__main__":
    # print(find_rounds([1, 2, 3, 4]))
    # # [[1, 2, 3, 4]]

    # print(find_rounds([1, 3, 2, 4]))
    # # [[1, 2], [3, 4]]    

    # print(find_rounds([4, 3, 2, 1]))
    # # [[1], [2], [3], [4]]
    
    # print(find_rounds([1]))
    # # [[1]]

    # print(find_rounds([2, 1, 4, 7, 5, 3, 6, 8]))
    # [[1], [2, 3], [4, 5, 6], [7, 8]]


    print(find_rounds([5,4,3,2,1]))


