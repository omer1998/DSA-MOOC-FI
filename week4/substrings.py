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
    
    return len(unique_substr)

if __name__ == "__main__":
    print(count_substrings("aaaa")) # 4
    print(count_substrings("abab")) # 7
    print(count_substrings("abcd")) # 10
    print(count_substrings("abbbbbb")) # 13
    print(count_substrings("aybabtu")) # 26
    print(count_substrings("saippuakauppias")) # 110