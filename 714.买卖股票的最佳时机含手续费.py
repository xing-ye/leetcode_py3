#
# @lc app=leetcode.cn id=714 lang=python3
#
# [714] 买卖股票的最佳时机含手续费
#

# @lc code=start


class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        # 动态规划
        n=len(prices)
        if n==0:
            return 0
        dp=[[0]*2 for _ in range(n)]
        dp[0][0]=-prices[0]
        for i in range(1,n):
            dp[i][0]=max(dp[i-1][0],dp[i-1][1]-prices[i])
            dp[i][1]=max(dp[i-1][1],dp[i-1][0]+prices[i]-fee)
            # 一次买入加卖出才是完整的交易
        return dp[-1][1]


        '''
        # 贪心算法
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
        '''


# @lc code=end

'''
贪心方法和动态规划方法，贪心不太好理解
dp[i][0] 表示第i天持有股票所省最多现金。 
dp[i][1] 表示第i天不持有股票所得最多现金
'''