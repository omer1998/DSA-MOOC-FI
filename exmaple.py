

# play_list = [1,2,1,3,5,4,3,1]

# def max_length(songs):
#     """
#     --> The dictionary pos stores the position of the last occurrence of each song. 
#     --> The variable start keeps track of the earliest possible starting position of a non-repeating part ending at the current position, 
#     --> variable length is the length of the longest non-repeating play list part we have found so far.

#     The algorithm goes through the play list and:
#       updates start whenever it encounters a song that it has seen before. 
#       In such a case, the value of start can increase to avoid a repeat of the song.

# The time complexity of the algorithm is 
# O(n) thanks to the efficient dictionary operations based on hashing."""
#     n= len(songs)
#     pos = {}
#     start = 0
#     length = 0
    
#     for i, song in enumerate(songs):
#         if song in pos:
#             start = max(start, pos[song]+1)

#         length = max(length, i-start +1)
#         pos[song] = i
#     return length

# print(max_length(songs=play_list))

nums = [2,3,5,-3,4,4,6,2]

def count_sublist(numbers, x):
    count = {0:1}
    prefix_sum = 0
    result = 0

    for i, num in enumerate(numbers):
        prefix_sum += num

        if prefix_sum - x  in count:
            result += count[prefix_sum-x]
        if prefix_sum  not in count:
            count[prefix_sum] = 0
        count[prefix_sum] += 1

    return result
    
# print(count_sublist(nums, 2))

nums = [4,10,7,21]
def two_sum(nums, x):
    result = []
    pos= {}
    for i, num in enumerate(nums):
        if num not in pos:
            pos[num] = i
        if x-num in pos:
            result = [i, pos[x-num]]
            return result
    return result



def two_sum2(nums,x):
    complements = {}

    for i, num in enumerate(nums):
        if num not in complements:
            complements[x-num] = i
        else:
            return [i, complements[num]]
    
    return []

# print(two_sum(nums, 25))
print(two_sum2(nums, 25))
