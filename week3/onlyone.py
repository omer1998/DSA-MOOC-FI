def find_number(numbers):
    """
    --> The list contains n-1 copies of the same number and a single copy of another number. Your task is to find what number occurs only once.
    --> implement the function find_number that takes the list of numbers as a parameter and returns the number with one occurrence only. 
    --> You may assume that the list contains at least three numbers so that the answer is always unique.
    """
  
    # [1, 1, 2, 1]
    nums_dict = {} # num : unique(True)
    
    for num in numbers:
        if num in nums_dict:
            nums_dict[num] = False
        else:
            nums_dict[num] = True
    
    for i in nums_dict:
        if nums_dict[i] == True:
            return i

        
                




if __name__ == "__main__":
    print(find_number([1, 1, 1, 2])) # 2
    print(find_number([1, 1, 2, 1])) # 2
    print(find_number([1, 2, 1, 1])) # 2
    print(find_number([2, 1, 1, 1])) # 2
    print(find_number([5, 5, 5, 3, 5])) # 3
    print(find_number([1, 100, 1])) # 100

    numbers = [1] * 10**5 + [2]
    print(find_number(numbers)) # 2