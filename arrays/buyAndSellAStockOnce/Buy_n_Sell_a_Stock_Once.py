#!/usr/bin/python3

#Buy n sell stock once to maximizing profit
# First buy then sell
# Optimized

prices = [310, 315, 275, 295, 260, 270, 290, 230, 255, 250]


def Buy_n_sell_stock_once(prices):
    
    min_price_so_far  = float('inf') 
    max_profit = 0.0

    for price in prices:
        max_profit_sell_today = price - min_price_so_far
        max_profit = max(max_profit, max_profit_sell_today)  
        min_price_so_far = min(min_price_so_far, price)
    
    return max_profit

print("The maximized profit: ", Buy_n_sell_stock_once(prices))