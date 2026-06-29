
prices = [3,2,6,4,8,3,1,5]
'''lower_price =  10**4
max_profit = 0 
upper_price = 0
for i in range(len(prices)):
    if i == len(prices)-1:
        max_profit = 0
    elif upper_price < prices[i+1]:
        upper_price = prices[i+1]
        profit = upper_price - prices[i]
        if max_profit <profit:
            max_profit = profit

print(max_profit) '''

min_price = 10**4
max_profit = 0
        
for price in prices:
    if price < min_price:
        min_price = price
           
    elif price - min_price > max_profit:
        max_profit = price - min_price
    
print(min_price) 
print(max_profit)        

    
        
