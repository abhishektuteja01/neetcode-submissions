class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i,j,res = 0,1,0
        
        while j < len(prices):
            if prices[j] < prices[i]:
                i = j
            res = max(res,prices[j]-prices[i])
            j+=1
        return res
        