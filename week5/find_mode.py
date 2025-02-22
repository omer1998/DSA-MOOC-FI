import random
import time
def find_mode_sorted(numbers:list):
    """
    Another efficient way to find a mode is to sort the elements and go through the list from left to right while keeping track of how many times each element is repeated.
Compare the efficiency of the above two solutions for an input list containing 10^7 random numbers in the range 1 \dots 1000."""

    sorted_nums = sorted(numbers)
    max_reccurence = 0
    mode = sorted_nums[0]
    result = ( max_reccurence, mode)
   
    
    start = time.time()
    for num in sorted_nums:
        if num == mode:
            max_reccurence +=1
            
        else:
            result = max(result, (max_reccurence, mode))
            mode = num
            max_reccurence = 1
    end = time.time()
    print("sort method last: ", end-start , "seconds")
    
    return result


def find_mode_Dictionary(numbers:list):
    """
    Another efficient way to find a mode is to sort the elements and go through the list from left to right while keeping track of how many times each element is repeated.
Compare the efficiency of the above two solutions for an input list containing 10^7 random numbers in the range 1 \dots 1000."""
    num_dict = {}# number, max_occurence
    start = time.time()
    
    result = (1,numbers[0] ) # occurance, num

    for num in numbers:
        if num not in num_dict:
            num_dict[num] = 0
        num_dict[num] += 1
        result = max(result,(num_dict[num], num) )
    
    # print("dict length: ", len(num_dict.keys()))
    # print(num_dict)
    # print(result)
    # for num in num_dict:
    #     n = num
    #     occurance = num_dict[n]
        
    #     result = max(result, (occurance,n))
    end = time.time()
    
    print("dict method last: ", end-start , "seconds")
    
    
    return result
    
    

    
if "__main__" == __name__:
    random.seed(1234)
    numbers = [random.randint(1,1000) for i in range(10**7 + 1)]
    # print(numbers[:10])
    # numbers = [2,4,5,3,5,4,3,6,3,54]
    print("sort method", find_mode_sorted(numbers=numbers))
    print("dict method", find_mode_Dictionary(numbers=numbers))