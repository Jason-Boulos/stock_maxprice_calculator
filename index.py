daily_stock_price_list = [1,5,10,20,30,5]


def max_profit(price_list):
    # check if the list has  less than 2 days and we just validate the case where there is no profitable buy options
    if len(price_list) < 2:
        return 0
    
    profit = 0
    # Loop through the list until the second last element
    for i in range(len(price_list) - 1):
        #  check if the next price is higher than the current price
        if price_list[i] < price_list[i + 1]:
            profit += price_list[i + 1] - price_list[i]
    
    return profit

# Example usage
print(max_profit(daily_stock_price_list))  
         
            
        
    
    
    
        
    
    