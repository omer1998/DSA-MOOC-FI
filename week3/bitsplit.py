def count_splits(sequence):
    """
    count how many ways the string can be split into two parts so that in both parts the number of 0s is equal to the number of 1s.

    For example, the string 010101 has two valid splits: 01+0101 and 0101+01. 
    In the part 01, both 0 and 1 occur once, and in the part 0101, both 0 and 1 occur twice.
    """
    balance = 0 # when zero mean potential split area but this need zero again in future iteration through the list
                # if we have 2 zero and the list is fished mean we have one split
                # if we have 2 zero and balance is not zero meaning there differant number of zero and one at the end of the list mean we cannot split anymore
                
    balance_num = 0
    for char in sequence:
        if char == "1":
            balance +=1
        elif char == "0":
            balance -= 1
        if balance == 0:
            balance_num +=1
    if balance < 0 or balance >=1:
        return 0
    # print("balance",balance)
    return balance_num -1


if __name__ == "__main__":
    print(count_splits("00")) # 0
    print(count_splits("01")) # 0
    print(count_splits("0110")) # 1
    print(count_splits("010101")) # 2
    print(count_splits("000111")) # 0
    print(count_splits("01100110")) # 3
    print(count_splits("10011011")) 

    sequence = "01"*10**5
    print(count_splits(sequence)) # 99999