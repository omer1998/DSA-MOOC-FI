from collections import deque
import time
def find_order(n):
    num_list= deque(range(1,n+1))
    skip = True
    order_list = []
    start = time.time()
    while num_list:
        if skip:
            num_list.append(num_list.popleft())
        else:
            order_list.append(num_list.popleft())
        skip = not skip
    end = time.time()
    
    return order_list, end-start



if __name__ == "__main__":
    print(find_order(1)) # [1]
    print(find_order(2)) # [2, 1]
    print(find_order(3)) # [2, 1, 3]
    print(find_order(7)) # [2, 4, 6, 1, 5, 3, 7]

    order, time= find_order(10**5)
    print(order[-5:], time) # [52545, 85313, 36161, 3393, 68929]