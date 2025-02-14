import random
import time


# implementation 1
def count_even(numbers):
    result = 0
    for x in numbers:
        if x % 2 == 0:
            result += 1
    return result

# implementation 2
def count_even2(numbers):
    return sum(x % 2 == 0 for x in numbers)


def main():
    random.seed(100)
    num_list = [random.randrange(0,10**7) for i in range(10**7)]
    
    start = time.time()
    count_even2(num_list)
    end = time.time()
    result = end- start
    print(result)


    start = time.time()
    count_even(num_list)
    end = time.time()
    result = end- start
    print(result)

    


main()
