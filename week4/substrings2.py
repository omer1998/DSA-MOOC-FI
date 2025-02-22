# import itertools


# print(list(itertools.combinations(range(5),2)))y
def count_substrings(string):
    """
    Counts distinct substrings using rolling hash for efficiency.
    """
    base1, mod1 = 911382629, 10**18 + 3
    base2, mod2 = 3571428571, 10**18 + 7

    n = len(string)
    prefix_hash1 = [0] * (n + 1)
    prefix_hash2 = [0] * (n + 1)
    power1 = [1] * (n + 1)
    power2 = [1] * (n + 1)

    for i in range(n):
        prefix_hash1[i+1] = (prefix_hash1[i] * base1 + ord(string[i])) % mod1
        prefix_hash2[i+1] = (prefix_hash2[i] * base2 + ord(string[i])) % mod2
        power1[i+1] = (power1[i] * base1) % mod1
        power2[i+1] = (power2[i] * base2) % mod2

    unique_hashes = set()

    for i in range(n):
        for j in range(i + 1, n + 1):
            # Compute hash for substring string[i:j]
            hash1 = (prefix_hash1[j] - prefix_hash1[i] * power1[j - i]) % mod1
            hash2 = (prefix_hash2[j] - prefix_hash2[i] * power2[j - i]) % mod2
            unique_hashes.add((hash1, hash2))

    return len(unique_hashes)

if __name__ == "__main__":
    print(count_substrings("aaaa"))        # 4
    print(count_substrings("abab"))        # 7
    print(count_substrings("abcd"))        # 10
    print(count_substrings("abbbbbb"))     # 13
    print(count_substrings("aybabtu"))     # 26
    print(count_substrings("saippuakauppias"))  # 110