#
# @lc app=leetcode.cn id=279 lang=python3
#
# [279] 完全平方数
#

# @lc code=start
class Solution:
    def numSquares(self, n: int) -> int:
        nums=[i**2 for i in range(1,n+1) if i**2<=n]
        # 准备物品，完全平方数
        dp=[10**4]*(n+1)
        dp[0]=0
        # 先遍历物品, 再遍历背包
        for num in nums:
            for i in range(num,n+1):
                dp[i]=min(dp[i],dp[i-num]+1)
        return dp[n]
# @lc code=end
'''和换零钱一样
dp[j]：和为j的完全平方数的最少数量为dp[j]
dp[j] = min(dp[j - i * i] + 1, dp[j]);
i * i是就是为了表示完平方
dp[0]表示 和为0的完全平方数的最小数量，那么dp[0]一定是0。
非0下标的dp[j]一定要初始为最大值，这样dp[j]在递推的时候才不会被初始值覆盖。
完全背包：
如果求组合数就是外层for循环遍历物品，内层for遍历背包。
如果求排列数就是外层for遍历背包，内层for循环遍历物品。
'''
