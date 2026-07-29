class Solution:
    def maxProfit(self,prices:list[int])->int:
        maxP=0
        minBuy=prices[0]

        for sell in prices:
            maxP=max(maxP,sell-minBuy)
            minBuy=min(minBuy,sell)

        return maxP

solution=Solution()
prices=[7,1,5,3,6,4,1]
print(solution.maxProfit(prices))