#
# @lc app=leetcode.cn id=674 lang=python3
#
# [674] 最长连续递增序列
#

# @lc code=start
class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        length=len(nums)
        if length<=1:
            return length
        res=0
        dp=[1]*length
        for i in range(1,length):
            if nums[i]>nums[i-1]:
                dp[i]=max(dp[i],dp[i-1]+1)
            res=max(res,dp[i])

        return res
# @lc code=end
'''
dp[i]：以下标i为结尾的数组的连续递增的子序列长度为dp[i]。
因为本题要求连续递增子序列，所以就必要比较nums[i + 1]与nums[i]，而不用去比较nums[j]与nums[i] （j是在0到i之间遍历）。
'''
