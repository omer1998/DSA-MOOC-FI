def count_substrings(string):
    """
    count how many distinct substrings there are in a given string.
    For example, the string abab has 7 distinct substrings: a, b, ab, ba, aba, bab and abab.
    """
    unique_substr = set()
    for i in range(len(string)):
        if string[i] not in unique_substr:
            unique_substr.add(string[i])
        for m in range(i,len(string)):
            if string[i:m+1] not in unique_substr:
                unique_substr.add(string[i:m+1])
    
    return unique_substr

def create_distribution(string):
    distribution = {}
    unique_substr_set = count_substrings(string)

    for str in unique_substr_set:
        if len(str) not in distribution:
            distribution[len(str)] = 0
        distribution[len(str)] +=1
    return distribution



if __name__ == "__main__":
    print(create_distribution("aaaa"))
    # {1: 1, 2: 1, 3: 1, 4: 1}
    
    print(create_distribution("abab"))
    # {1: 2, 2: 2, 3: 2, 4: 1}
    
    print(create_distribution("abcd"))
    # {1: 4, 2: 3, 3: 2, 4: 1}

    print(create_distribution("abbbbbb"))
    # {1: 2, 2: 2, 3: 2, 4: 2, 5: 2, 6: 2, 7: 1}

    print(create_distribution("aybabtu"))
    # {1: 5, 2: 6, 3: 5, 4: 4, 5: 3, 6: 2, 7: 1}