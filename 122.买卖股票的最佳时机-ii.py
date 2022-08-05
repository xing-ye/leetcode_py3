#
# @lc app=leetcode.cn id=122 lang=python3
#
# [122] 买卖股票的最佳时机 II
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 动态规划
        length=len(prices)
        dp=[[0]*2 for _ in range(length)]
        dp[0][0]=-prices[0]
        dp[0][1]=0
        for i in range(1,length):
            dp[i][0]=max(dp[i-1][0],dp[i-1][1]-prices[i])  
            dp[i][1]=max(dp[i-1][1],dp[i-1][0]+prices[i]) 
        return dp[-1][1] 
        # 贪心算法
        '''
        res=0
        for i in range(1,len(prices)):
            dayV=prices[i]-prices[i-1]
            res+=max(dayV,0)
        return res
        '''
# @lc code=end

'''
动态规划：与121基本相同，唯一的区别在dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] - prices[i]);
这正是因为本题的股票可以买卖多次！ 所以买入股票的时候，可能会有之前买卖的利润即：dp[i - 1][1]，所以dp[i - 1][1] - prices[i]。
dp[i][0] 表示第i天持有股票所得最多现金 ，dp[i][1] 表示第i天不持有股票所得最多现金

贪心算法,实际上将问题分解为计算每天的利润,只要求的正利润之和即可
'''