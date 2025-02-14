def find_profits(prices):
    """
    --> that takes a list of prices as a parameter, and returns the list of profits.
    --> Your task is to compute for each day the highest profit you could have achieved by selling the stock on that day.
    --> For example, when the prices are [3,2,3,5,1,4], the desired answer is the list [0,0,1,3,0,3]. 
        For example, on the fourth day the maximum profit is 3, 
        because you could have bought the stock at the price 2 and sold it at the price 5.
    
    """
    profit_list = []
    first_price = 0

    for i in range(len(prices)):
        if i == 0:
            first_price = prices[i]
            profit_list.append(0)
        else:
            if prices[i] <= first_price:
                first_price = prices[i]
                profit_list.append(0)
            else:
                profit_list.append(prices[i]- first_price)
    return profit_list


if __name__ == "__main__":
    print(find_profits([1, 2, 3, 4])) # [0, 1, 2, 3]
    print(find_profits([4, 3, 2, 1])) # [0, 0, 0, 0]
    print(find_profits([1, 1, 1, 1])) # [0, 0, 0, 0]
    print(find_profits([2, 4, 1, 3])) # [0, 2, 0, 2]
    print(find_profits([1, 1, 5, 1])) # [0, 0, 4, 0]
    print(find_profits([3, 2, 3, 5, 1, 4])) # [0, 0, 1, 3, 0, 3]

    prices = list(range(1, 10**5+1))
    print(find_profits(prices)[:5]) # [0, 1, 2, 3, 4]