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


user_input = input('Enter elements of a list separated by space:\n')
user_list = user_input.split()

#validated list
valid_user_input = []

#  user input  validation
for item in user_list:
    if item.isdigit():  # lacks negative numbers
        valid_user_input.append(int(item))
    else:
        print(f"'{item}' is not a valid integer.")

result = max_profit(valid_user_input)
print(result)

         
            
        
    
    
    
        
    
    