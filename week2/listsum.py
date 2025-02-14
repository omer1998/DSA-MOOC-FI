def find_sums(numbers, size):
    """
    You are given a list of numbers and your task is to compute the sum of every sublist of a given size 
    from left to right.
    For example, when the list is [1,2,3,4,5] and the sublist size is 3, 
    the sublists are [1,2,3], [2,3,4] and [3,4,5]. The sums of the sublists are 6, 9 and 12.
    """
    sum_sublist = []
    index = 0
    first_sum = sum(numbers[0:size])
    sum_sublist.append(first_sum)
    while index < len(numbers):
        if index+size >= len(numbers):
            break
        new_sum = first_sum - numbers[index] + numbers[index+size]
        first_sum = new_sum
        sum_sublist.append(new_sum)
        index+=1
    return sum_sublist



    


if __name__ == "__main__":
    # print(find_sums([1], 1)) # [1]
    print(find_sums([1, 8, 2, 7, 3, 6, 4, 5], 6)) # [27, 30, 27]

    print(find_sums([1, 2, 3, 4, 5], 1)) # [1, 2, 3, 4, 5]
    print(find_sums([1, 2, 3, 4, 5], 2)) # [3, 5, 7, 9]
    print(find_sums([1, 2, 3, 4, 5], 3)) # [6, 9, 12]
    print(find_sums([1, 2, 3, 4, 5], 4)) # [10, 14]
    print(find_sums([1, 2, 3, 4, 5], 5)) # [15]

    numbers = list(range(10**5))
    sums = find_sums(numbers, 10**4)
    print(sums[5]) # 50045000
    print(sums[42]) # 50415000
    print(sums[1337]) # 63365000