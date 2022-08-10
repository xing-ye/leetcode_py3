#
# @lc app=leetcode.cn id=309 lang=python3
#
# [309] 最佳买卖股票时机含冷冻期
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n=len(prices)
        if n==0:
            return 0
        dp=[[0]*4 for _ in range(n)]
        dp[0][0]=-prices[0]
        for i in range(1,n):
            dp[i][0]=max(dp[i-1][0],max(dp[i-1][1]-prices[i],dp[i-1][3]-prices[i]))
            dp[i][1]=max(dp[i-1][1],dp[i-1][3])
            dp[i][2]=dp[i-1][0]+prices[i]
            # dp[i][2]与传统的不同，为今天卖出，所以不用保持这一状态
            # 它实际上与下一状态冷静期是一中大状态的划分
            dp[i][3]=dp[i-1][2]

        return max(dp[n-1][3], dp[n-1][1], dp[n-1][2])
# @lc code=end

'''
这个十分复杂，详见：
https://programmercarl.com/0309.%E6%9C%80%E4%BD%B3%E4%B9%B0%E5%8D%96%E8%82%A1%E7%A5%A8%E6%97%B6%E6%9C%BA%E5%90%AB%E5%86%B7%E5%86%BB%E6%9C%9F.html#%E6%80%9D%E8%B7%AF

dp[i][0] = max(dp[i - 1][0], max(dp[i - 1][3], dp[i - 1][1]) - prices[i]);
dp[i][1] = max(dp[i - 1][1], dp[i - 1][3]);
dp[i][2] = dp[i - 1][0] + prices[i];
dp[i][3] = dp[i - 1][2];
'''