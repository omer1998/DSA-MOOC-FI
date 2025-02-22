def create_string(pages: list):
    """"
    You are given a list of page numbers. Your task is to construct a string that describes the page ranges compactly.
If the list contains all page numbers in the range a \dots b, this should be presented in the form a–b. If the list contains an isolated page number, it should be presented as a single number. If the list contains multiple page ranges, they should be presented as an ordered list separated by commas. Repeated page numbers should be included only once.
For example, if the list is [3,2,9,4,3,6,9,8], the desired representation is 2-4,6,8-9.
"""
    
    numbers = pages.copy()
    numbers.sort() # sorting first
    numbers = sorted(set(numbers)) # remove dublicate
    # return numbers
  
    start = numbers[0]
    end = numbers[0]
    result = []
    for i in range(1, len(numbers)) :
        if numbers[i] == end +1 : # look for interval; if true mean number[i] is consecutive to the previous number
                                  # so extend interval 
            end = numbers[i]
        elif numbers[i] > end:  # not consecutive mean two things; either single num alone or this next interval, we 've put the previous interval but what we do in case of single num; single num mean start == end put either of them
            if start == end :
                result.append(str(start))
            else:
                result.append(str(start)+ "-"+ str(end))
            start = end = numbers[i]
    # put the final interval or single num
    if start == end :
        result.append(str(start))
    else:
        result.append(str(start)+ "-"+ str(end))
         

        

    return ",".join(result)




if __name__ == "__main__":
    # create_string([])
    print(create_string([1])) # 1
    print(create_string([1, 2, 3])) # 1-3
    print(create_string([1, 1, 1])) # 1
    print(create_string([1, 2, 1, 2])) # 1-2
    print(create_string([1, 6, 2, 5])) # 1-2,5-6
    print(create_string([1, 3, 5, 7])) # 1,3,5,7
    print(create_string([1, 8, 2, 7, 3, 6, 4, 5])) # 1-8
    print(create_string([3, 2, 9, 4, 3, 6, 9, 8])) # 2-4,6,8-9

    pages = [3, 2, 1, 3, 2, 1]
    print(create_string(pages)) # 1-3
    # print(pages) # [3, 2, 1, 3, 2, 1]