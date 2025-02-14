

# def find_rounds(numbers: list):
#     remaining_nums = set(numbers)
#     sorted_numbers = sorted(remaining_nums)
#     all_subsets = []
#     rounds_count = 0
    

#     while remaining_nums:
#         sub_set = []
#         smallest_num = min(remaining_nums)
#         current_num = smallest_num
#         while current_num in remaining_nums:
#             sub_set.append(current_num)
#             remaining_nums.remove(current_num)
#             current_num += 1


        
                

#             # else:
#             #     continue
#         all_subsets.append(sub_set)
#         rounds_count += 1

#     return all_subsets, rounds_count

def find_rounds(numbers: list):
    # if not numbers:
    #     return [], 0

    # # Sort the numbers once at the beginning
    # # sorted_numbers = sorted(numbers)
    # remaining_nums = set(numbers)  # Use a set for O(1) lookups and removals
    # all_subsets = []
    # rounds_count = 0

    # # num_dic key: number in numbers, value: index

    # num_dict ={}
    # for i in range(len(numbers)):
    #     num_dict[numbers[i]] = i

    # while remaining_nums:
    #     # Find the smallest remaining number
    #     smallest_num = min(remaining_nums)
    #     sub_set = []
    #     sub_set.append(smallest_num)
    #     remaining_nums.remove(smallest_num)
    #     current_num = smallest_num
    #     index = num_dict[current_num]
    #     # Build the subset of consecutive numbers
    #     for num in numbers[index+1:]:
    #         if num == current_num+1:
    #             sub_set.append(num)
    #             current_num += 1
    #             remaining_nums.remove(num)


    #     all_subsets.append(sub_set)
    #     rounds_count += 1
    if not numbers:
        return [], 0
    
    # Sort numbers and remove duplicates while preserving order
    sorted_unique = sorted(set(numbers), key=numbers.index)
    
    all_subsets = []
    i = 0
    
    while i < len(sorted_unique):
        # Start a new round with the current number
        current_round = [sorted_unique[i]]
        current_max = sorted_unique[i]
        
        # Find consecutive numbers in this round
        j = i + 1
        while j < len(sorted_unique) and sorted_unique[j] == current_max + 1:
            current_round.append(sorted_unique[j])
            current_max = sorted_unique[j]
            j += 1
        
        # Add the round and move to the next unprocessed number
        all_subsets.append(current_round)
        i = j

    return all_subsets, len(all_subsets)



if __name__ == "__main__":
    print(find_rounds([1, 6, 7, 2, 3, 4, 5]))
    # [[1, 2, 3, 4, 5], [6, 7]]
    
    print(find_rounds([1, 3, 2, 4]))
    # [[1, 2], [3, 4]]