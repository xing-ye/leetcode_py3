#
# @lc app=leetcode.cn id=121 lang=python3
#
# [121] 买卖股票的最佳时机
#

# @lc code=start


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 贪心算法
        # low=float('inf')
        # result=0
        # for i in range(len(prices)):
        #     low=min(low,prices[i])
        #     result=max(result,prices[i]-low)
        # return result
        # 动态规划
        length=len(prices)
        if length==0:
            return 0
        dp=[[0]*2 for _ in range(len(prices))]
        dp[0][0]=-prices[0]
        dp[0][1]=0
        for i in range(1,length):
            dp[i][1]=max(dp[i-1][1],dp[i-1][0]+prices[i])
            dp[i][0]=max(dp[i-1][0],-prices[i])
            # 0就是算什么时候买最便宜，1就是什么时候买挣得最多
        return dp[-1][1]

# @lc code=end

'''
dp[i][0] 表示第i天持有股票所得最多现金 
dp[i][1] 表示第i天不持有股票所得最多现金
注意这里说的是“持有”，“持有”不代表就是当天“买入”！也有可能是昨天就买入了，今天保持持有的状态
dp[i][0] = max(dp[i - 1][0], -prices[i]); dp[0][0] -= prices[0]
dp[i][1] = max(dp[i - 1][1], prices[i] + dp[i - 1][0]); dp[0][1] = 0
'''