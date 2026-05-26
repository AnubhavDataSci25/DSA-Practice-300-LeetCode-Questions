"""
LeetCode Question 121: Best time to Buy and Sell Stock

You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
"""

def max_profit(prices):
    maxProfit = 0
    best_buy = prices[0]
    for i in range(0,len(prices)):
        if prices[0] > best_buy:
            maxProfit = max(maxProfit, prices[i]-best_buy)
        best_buy = min(best_buy, prices[i])
    return maxProfit

prices = [7,1,5,3,6,4]
max_prof = max_profit(prices)
print(max_prof)