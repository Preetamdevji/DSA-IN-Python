# Figure out the best day to buy and the best future day to sell, so that you can make the maximum profit.

prices = [7, 1, 5, 3, 6, 4]

def maximum_profit(prices):
    
    min_price = prices[0]
    max_profit = 0
    for price in prices:
        today_profit = price - min_price

        if today_profit > max_profit:
            max_profit = today_profit

        if price < min_price:
            min_price = price
        print("Maximum Profit:", max_profit)

maximum_profit(prices)
