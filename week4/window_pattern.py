

# finding maximum sum 
# Problem: Find the maximum sum of a subarray of size k

def find_max_subarr_sizeK(numbers:list,k):
    window_sum = sum(numbers[:k])
    max_sum_index = [i for i in range(k)]
    max_sum_list = [numbers[i] for i in range(k)]
    max_sum = window_sum

    for right in range(k, len(numbers)):
        window_sum += numbers[right] - numbers[right-k]
        if window_sum > max_sum:
            max_sum_index = [ i for i in range(right-k,right)]
            max_sum_list = [ numbers[i] for i in range(right-k,right)]
        window_sum = max(max_sum, window_sum)
    return max_sum,max_sum_index, max_sum_list

print(find_max_subarr_sizeK([5,3,6,2,4,6,3,4,6,3,7,4], 5))


