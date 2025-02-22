import time
def find_distances(street):
    """
    given a string that describes a row of buildings on a street. Each character is either 0 (house) or 1 (shop).
    Your task is to construct a list that tells for each building, what is the shortest distance from the building to a shop. 
    If the building is a shop, the distance is 0.
    For example, if the buildings are 00100010, the desired list is [2,1,0,1,2,1,0,1]. If the buildings are 00100000, the list is [2,1,0,1,2,3,4,5]. You may assume that at least one of the buildings is a shop."""

    # get shops place index0 place in the street
    # shops_place_index = []  
    # for i in range(len(street)):
    #     if street[i] == "1":
    #         shops_place_index.append(i)
    # start_time = time.time()

    # shortest_path = []

    # for b in range(len(street)):
    #     min_path = abs(shops_place_index[0]- b)
    #     if len(shops_place_index) > 1:
    #         for shop_index in shops_place_index:
    #             min_path = min(min_path, abs(shop_index-b))
    #     shortest_path.append(min_path)
    
    # end_time = time.time()
    # # print("length shops_place_index ", len(shops_place_index))
    # print("time", end_time- start_time)

    # second approach 2 pass approach; 
    # one pass from left to right to keep track of the last shop index
    # second pass from right to left to keep track of the next shop index
    start_time = time.time()
    
    street_length = len(street)
    # initialize 
    shortest_path_list = [street_length] * street_length 

    # first pass; left to right to keep track the last_shop_index
    last_shop_index= street_length + 10

    for i in range(street_length):
        if street[i] == "1": # shop
            shortest_path_list[i] = 0
            last_shop_index = i
        else:
            shortest_path_list[i] = last_shop_index - i

    # second pass from right to left; keep track of the next_shop_index

    next_shop_index= last_shop_index

    for n in range(street_length-1, -1, -1):
        if street[n] == "1":
            next_shop_index = n
        else:
            shortest_path_list[n] = min(abs(shortest_path_list[n]), abs(next_shop_index- n))
    end_time = time.time()
    print("last: ", end_time-start_time , "seconds")
    return shortest_path_list


        



    
        


if __name__ == "__main__":
    print(find_distances("00100010")) # [2, 1, 0, 1, 2, 1, 0, 1]
    print(find_distances("00100000")) # [2, 1, 0, 1, 2, 3, 4, 5]
    print(find_distances("11111111")) # [0, 0, 0, 0, 0, 0, 0, 0]
    print(find_distances("01010101")) # [1, 0, 1, 0, 1, 0, 1, 0]
    print(find_distances("10000000")) # [0, 1, 2, 3, 4, 5, 6, 7]
    print(find_distances("00000001")) # [7, 6, 5, 4, 3, 2, 1, 0]

    n = 10**5
    street = "0"*n + "1" + "0"*n
    distances = find_distances(street)
    print(distances[1337]) # 98663