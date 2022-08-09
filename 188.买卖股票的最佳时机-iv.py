#
# @lc app=leetcode.cn id=188 lang=python3
#
# [188] 买卖股票的最佳时机 IV
#

# @lc code=start
class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        if len(prices) == 0:
            return 0
        dp=[[0]*(2*k+1) for _ in range(len(prices))]
        # K为交易次数
        for i in range(1,2*k,2):
            dp[0][i]=-prices[0]
        for i in range(1,len(prices)):
            for j in range(0,2*k-1,2):
                # 这里只能到2k-2，因为推到公式里J在后面
                # 这里只是算后一步的买入和卖出即可
                dp[i][j+1]=max(dp[i-1][j+1],dp[i-1][j]-prices[i])
                dp[i][j+2]=max(dp[i-1][j+2],dp[i-1][j+1]+prices[i])
        return dp[-1][2*k]
# @lc code=end

'''
实际上就是把123题进行了总结：可以看到，偶数为卖出，初始化为0，奇数为买入初始化为-prices[i]

这里设置了5个
0：没有操作
1：第一次买入
2：第一次卖出
3：第二次买入
4：第二次卖出
dp[i][j]中 i表示第i天，j为 [0 - 4] 五个状态，dp[i][j]表示第i天状态j所剩最大现金。
'''