#
# @lc app=leetcode.cn id=123 lang=python3
#
# [123] 买卖股票的最佳时机 III
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        length= len(prices)
        if length==0:
            return 0
        dp=[[0]*5 for _ in range(length)]
        dp[0][0]=0
        dp[0][1]=-prices[0]
        dp[0][2]=0
        dp[0][3]=-prices[0]
        # 第二次买入依赖于第一次卖出的状态，其实相当于第0天第一次买入了，第一次卖出了，然后在买入一次（第二次买入），那么现在手头上没有现金，只要买入，现金就做相应的减少。
        dp[0][4]=0
        for i in range(1,length):
            dp[i][1]=max(dp[i-1][1],dp[i-1][0]-prices[i])
            dp[i][2]=max(dp[i-1][2],dp[i-1][1]+prices[i])
            dp[i][3]=max(dp[i-1][3],dp[i-1][2]-prices[i])
            dp[i][4]=max(dp[i-1][4],dp[i-1][3]+prices[i])
        return dp[-1][4]
# @lc code=end

'''
这里设置了5个
0：没有操作
1：第一次买入
2：第一次卖出
3：第二次买入
4：第二次卖出
dp[i][j]中 i表示第i天，j为 [0 - 4] 五个状态，dp[i][j]表示第i天状态j所剩最大现金。
'''