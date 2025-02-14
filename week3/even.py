# def count_sublists(numbers):
#     """
#     count how many sublists contain only even numbers.
#     """
#     start = 0
#     is_even= False
#     for i,num in enumerate(numbers):
#         if is_even == True and num % 2 ==0:
#             start += i+1
#         elif num % 2== 0:
#             is_even = True
#             start +=1 
#         else:
#             is_even = False
#     return start

def count_sublists(numbers):

    even_length = 0
    count = 0

    for num in numbers:
        if num % 2 ==0:
            even_length +=1
            count += even_length
            
        else:
            even_length = 0
    return count



if __name__ == "__main__":
    print(count_sublists([2, 4, 1, 6])) # 4
    print(count_sublists([1, 2, 3, 4])) # 2
    print(count_sublists([1, 1, 1, 1])) # 0
    print(count_sublists([2, 2, 2, 2])) # 10
    print(count_sublists([1, 1, 2, 1])) # 1
    print(count_sublists([2, 4]))

    numbers = [2] * 10**5
    print(count_sublists(numbers)) # 5000050000