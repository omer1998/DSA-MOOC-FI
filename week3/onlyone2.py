import collections

def find_number(numbers):
    """
    --> The list contains n-1 copies of the same number and a single copy of another number. Your task is to find what number occurs only once.
    --> implement the function find_number that takes the list of numbers as a parameter and returns the number with one occurrence only. 
    --> You may assume that the list contains at least three numbers so that the answer is always unique.
    """
  
    # [1, 1, 2, 1]
    # # # mathmatical method
    # list_sum = sum(numbers)
    # repeated_num = max(set(numbers), key=numbers.count)
    # nums_length = len(numbers)

    # unique_num = list_sum - repeated_num * (nums_length-1)
    # return unique_num

    # # # using collections

    counters= collections.Counter(numbers)
    for num, count in counters.items():
        if count == 1:
            return num
    
        
                




if __name__ == "__main__":
    print(find_number([1, 1, 1, 2])) # 2
    print(find_number([1, 1, 2, 1])) # 2
    print(find_number([1, 2, 1, 1])) # 2
    print(find_number([2, 1, 1, 1])) # 2
    print(find_number([5, 5, 5, 3, 5])) # 3
    print(find_number([1, 100, 1])) # 100

    numbers = [1] * 10**5 + [2]
    print(find_number(numbers)) # 2