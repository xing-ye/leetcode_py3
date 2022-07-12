#
# @lc app=leetcode.cn id=518 lang=python3
#
# [518] 零钱兑换 II
#

# @lc code=start
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp=[0]*(amount+1)
        dp[0]=1
        for i in range(len(coins)):
            for j in range(coins[i],amount+1):
                dp[j]+=dp[j-coins[i]]
        return dp[amount]
# @lc code=end

'''
不限制物品的数量实际上就是，完全背包
但本题和纯完全背包不一样，纯完全背包是能否凑成总金额，而本题是要求凑成总金额的个数！

dp[j]：凑成总金额j的货币组合数为dp[j]
dp[j] += dp[j - coins[i]];
组合不强调元素之间的顺序，排列强调元素之间的顺序。因为，本题问的是组合数而对于背包来说，对于顺序并不要求，即有顺序也行，没有顺序也行！
这就要求，我们先遍历物品，在遍历背包容量，防止出现组合相同但顺序不同的被计算
'''