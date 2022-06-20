#
# @lc app=leetcode.cn id=714 lang=python3
#
# [714] 买卖股票的最佳时机含手续费
#

# @lc code=start


class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        res=0
        minPrice=prices[0]
        for i in range(1,len(prices)):
            if prices[i]<minPrice:
                minPrice=prices[i] #找到最小买入时间
                # 不用担心会错过，因为卖出一定在买入后。
            elif prices[i]>=minPrice and prices[i]<=minPrice+fee:
                continue
            else:
                res+=prices[i]-minPrice-fee
                # 减去买入点和手续费
                minPrice=prices[i]-fee
                # 这时候最小的至少是要小于这个点，
                # 而且带进去，其实就是prices[i]-price[j]，相当于后面是加了差值
        return res



# @lc code=end

'''
贪心方法和动态规划方法，贪心不太好理解
'''