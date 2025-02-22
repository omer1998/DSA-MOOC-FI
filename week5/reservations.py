import random

def check_overlapping(reservations):
    """
    You are given a list containing reservations as day ranges. Each range is a pair (a,b), where 1 \le a \le b: the reservation starts on the day a and ends on the day b.
Your task is to determine if the list contains two overlapping reservations, i.e., two ranges with one or more common days.
For example, the list [(4,7),(1,2)] means that the first reservation is from the day 4 to the day 7, 
and the second reservation is from the day 1 to the day 2. These two reservations do not ovelap. 
On the other hand, the reservations on the list [(4,7),(1,5)] do overlap, 
because both ranges contain the days 4 and 5."""

    if len(reservations) <= 1:
        return False
    
    sorted_reservations = sorted(reservations, key=lambda x:x[0])
    first_resv = sorted_reservations[0]
    for i in range(1,len(sorted_reservations)):
        start_day = sorted_reservations[i][0]
        if start_day <= first_resv[1]:
            return True
        first_resv = sorted_reservations[i]
    
    return False 

if __name__ == "__main__":
    print(check_overlapping([])) # False
    print(check_overlapping([(1, 3)])) # False
    print(check_overlapping([(4, 7), (1, 2)])) # False
    print(check_overlapping([(4, 7), (1, 5)])) # True
    print(check_overlapping([(1, 1), (2, 2)])) # False
    print(check_overlapping([(1, 1), (1, 1)])) # True
    print(check_overlapping([(2, 3), (5, 5), (3, 4)])) # True
    print(check_overlapping([(2, 3), (5, 5), (1, 4)])) # True
    print(check_overlapping([(2, 3), (5, 5), (1, 5)])) # True

    reservations = [(day, day) for day in range(1, 10**5+1)]
    random.shuffle(reservations)
    print(check_overlapping(reservations)) # False

    reservations.append((42, 1337))
    random.shuffle(reservations)
    print(check_overlapping(reservations)) # True