#
# @lc app=leetcode.cn id=198 lang=python3
#
# [198] 打家劫舍
#

# @lc code=start
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        dp = [0] * len(nums)
        # 这里不需要nums+1是因为nums[n+1]不存在啊。
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for i in range(2, len(nums)):
            dp[i] = max(dp[i-2]+nums[i], dp[i-1])
        return dp[-1]
# @lc code=end

'''
这个不是背包问题了
dp[i]：考虑下标i（包括i）以内的房屋，最多可以偷窃的金额为dp[i]。
dp[i] = max(dp[i - 2] + nums[i], dp[i - 1])
如果偷第i个房间，那么dp[i] = dp[i - 2] + nums[i] 
如果不偷第i房间，那么dp[i] = dp[i - 1]，即考虑i-1房

从dp[i]的定义上来讲，dp[0] 一定是 nums[0]，dp[1]就是nums[0]和nums[1]的最大值即：dp[1] = max(nums[0], nums[1]);
'''