from collections import deque
import time

def find_order(n):
    # [1,2,3,4,5,6,7,8,9]
    start = time.time()
    num_list = deque([i for i in range(1,n+1)])
    order_list = []
    skip = True
    path= []
    while num_list:
        if skip:
            first_num = num_list[0]
            num_list.popleft()
            num_list.append(first_num)
        else:
            order_list.append(num_list[0])
            num_list.popleft()
        if skip:
            skip =False
        else:
            skip = True
    end = time.time()
    return order_list, end-start

            



if __name__ == "__main__":
    print(find_order(1)) # [1]
    print(find_order(2)) # [2, 1]
    print(find_order(3)) # [2, 1, 3]
    print(find_order(7)) # [2, 4, 6, 1, 5, 3, 7]

    order, time = find_order(10**5)
    print(order[-5:], time) # [52545, 85313, 36161, 3393, 68929]