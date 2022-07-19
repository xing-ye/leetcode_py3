#
# @lc app=leetcode.cn id=322 lang=python3
#
# [322] 零钱兑换
#

# @lc code=start
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp=[amount+1]*(amount+1)
        # 这里初始化为比较大的数，是因为后面要min，否则会被覆盖
        dp[0]=0# 因为总额为0，那么肯定能够最小数目就是0
        for coin in coins:
            for i in range(coin,amount+1):
                dp[i]=min(dp[i],dp[i-coin]+1)

        return dp[amount] if dp[amount]<amount+1 else -1
        # 这是为了对于一个总额为amount的，组成它的数量一定不可能超过amount
# @lc code=end

'''
完全背包，
dp[j]：凑足总额为j所需钱币的最少个数为dp[j]
这种最小、最大的，不是求总量或者种类数，所以需要max或者min
这里不强调顺序，所以先遍历物品就可以了
'''
