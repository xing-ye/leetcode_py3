#
# @lc app=leetcode.cn id=300 lang=python3
#
# [300] 最长递增子序列
#

# @lc code=start
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if len(nums)<=1:
            return len(nums)
        dp=[1]*len(nums)
        res=0
        for i in range(1,len(nums)):
            for j in range(0,i):
                if nums[i]>nums[j]:
                    dp[i]=max(dp[i],dp[j]+1)
            res=max(res,dp[i])
        return res
# @lc code=end
'''
dp[i]表示i之前包括i的以nums[i]结尾最长上升子序列的长度
位置i的最长升序子序列等于j从0到i-1各个位置的最长升序子序列 + 1 的最大值。
if (nums[i] > nums[j]) dp[i] = max(dp[i], dp[j] + 1);
每一个i，对应的dp[i]（即最长上升子序列）起始大小至少都是1.
'''

