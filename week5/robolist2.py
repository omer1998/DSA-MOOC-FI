def count_steps(numbers):
    """
    You are given a list of integers. No number occurs more than once on the list.
A robot starts at the location 0 and collects the numbers on the list in order from the smallest to the largest. Your task is to compute how many steps the robot takes in total.
For example, when the list is [42, 1337, 1, 10^9], the robot moves as follows:

2 steps to the right (number 1)
2 steps to the left (number 42)
1 step to the right (number 1337)
2 steps to the right (number 10^9)

In this case, the robot takes 2+2+1+2=7 steps.
"""
    
    sorted_nums = sorted(numbers)
    sorted_nums_set = set(sorted_nums)
    
    prev_num_index = 0
    total_steps = 0
    sorted_num_index = 0
    # print(sorted_nums_dict[0])
    
    i = 0
    while sorted_nums_set:
        if sorted_nums[sorted_num_index] == numbers[i]:
            total_steps += abs(i-prev_num_index)
            prev_num_index = i
            sorted_num_index +=1
            sorted_nums_set.remove(numbers[i])
            i = 0
            continue
        i +=1
    return total_steps

if __name__ == "__main__":
    print(count_steps([1])) # 0
    print(count_steps([1, 2, 3])) # 2
    print(count_steps([3, 2, 1])) # 4
    print(count_steps([42, 1337, 1, 10**9])) # 7
    print(count_steps([1, 3, 5, 7, 8, 6, 4, 2])) # 28
    print(count_steps([10**6, 10**8, 10**7, 10**9])) # 5

    # numbers = [(x * 999983) % 10**9 + 1 for x in range(10**5)]
    # print(count_steps(numbers)) # 4871908997