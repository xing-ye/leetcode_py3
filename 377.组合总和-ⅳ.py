#
# @lc app=leetcode.cn id=377 lang=python3
#
# [377] 组合总和 Ⅳ
#

# @lc code=start
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp=[0]*(target+1)
        dp[0]=1
        for i in range(1,target+1):
            for j in range(len(nums)):
                if i>=nums[j]:
                    dp[i]+=dp[i-nums[j]]
        return dp[target]
# @lc code=end

'''
个数可以不限使用，说明这是一个完全背包。
以前先遍历物品，是为了防止有重复的出现例如[1,3],[3,1]
现在不同顺序是可以的，所以应该先遍历背包在遍历物品
dp[i]: 凑成目标正整数为i的排列个数为dp[i]
dp[0] = 1是没有意义的，仅仅是为了推导递推公式。
'''