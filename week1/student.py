def check_number(number):
    first = number[0]
    last = number[-1] # which is the check digit
    other_digits = number[0:-1]
    checking_digits = "37137137"
    index= 0
    if len(other_digits) != len(checking_digits):
        return False
    if int(first) != 0:
        return False
    sum =0
    while index < len(other_digits):
        sum = sum + int(other_digits[index]) * int(checking_digits[index])
        index = index + 1
    if sum % 10 == 0:
        if int(last) == 0:
            return True
        else:
            return False
    m_ten = 10
    
    while m_ten < sum:
        m_ten = m_ten + 10
    # print(last)
    # print(m_ten)
    # print(sum)
    distance_to_next_10_multiple = m_ten-sum
    if int(last) == (m_ten-sum):
        return True
    return False 





if __name__ == "__main__":
    print(check_number("012749138")) # False
    print(check_number("012749139")) # True
    print(check_number("013333337")) # True
    print(check_number("012345678")) # False
    print(check_number("012344550")) # True
    print(check_number("1337")) # False
    print(check_number("0127491390")) # False
    print(check_number("100000007"))