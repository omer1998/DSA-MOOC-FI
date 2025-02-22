import string as strr
def hash_value(string):
    """
    Consider the following hash function:
$$
(c_0 A^{n-1} + c_1 A^{n-2} \cdots + c_{n-1} A^0) \bmod M
$$
The function computes a hash value of a string consisting of the characters c_0,c_1,\dots,c_{n-1}. Each character is in the range a–z, and the characters have been coded so that a is 0, b is 1 etc.. The function involves two constants with the values A=23 and M=2^{32}.

    """
    

    char_code = {
        chr(i+96): i-1 for i in range(1,27)
    }
    # print(char_code)
    
    init = 1
    str_length = len(string)
    res = 0
    for char in string:
        
        res += char_code[char] * (23**(str_length - init))
        init +=1
    res = res % (2**32)

    return res


if __name__ == "__main__":
    print(hash_value("abc")) # 25
    print(hash_value("kissa")) # 2905682
    print(hash_value("aybabtu")) # 154753059
    print(hash_value("tira")) # 235796
    print(hash_value("zzzzzzzzzz")) # 2739360440
    print(hash_value("kissa"))