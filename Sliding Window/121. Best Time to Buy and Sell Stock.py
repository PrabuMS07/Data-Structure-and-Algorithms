"""You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

 

Example 1:

Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
"""

class Solution(object):
    def maxProfit(self, prices):
        max_p = 0
        l = 0
        r = 1
        while r < len(prices):
            if prices[r] > prices[l]:
                cur_p = prices[r] - prices[l]
                if cur_p > max_p:
                    max_p = cur_p
            else:
                l = r
            r+=1
        return max_p

obj = Solution()

print(obj.maxProfit(prices = [7,1,5,3,6,4]))