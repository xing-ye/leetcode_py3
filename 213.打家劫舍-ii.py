#
# @lc app=leetcode.cn id=213 lang=python3
#
# [213] 打家劫舍 II
#

# @lc code=start



class Solution:
    def rob(self, nums: List[int]) -> int:
        #在198入门级的打家劫舍问题上分两种情况考虑
        #一是不偷第一间房，二是不偷最后一间房
        if len(nums)==1:
            return nums[0]
        if len(nums)==2:
            return max(nums[0],nums[1])
        val1=self.robRange(nums[1:])
        val2=self.robRange(nums[:-1])
        return max(val1,val2)

    def robRange(self,nums):
        length=len(nums)
        # 能过来的至少是length=2
        if length==2:
            return max(nums[0],nums[1])
        dp=[0]*length
        dp[0]=nums[0]
        dp[1]=max(nums[0],nums[1])
        for i in range(2,length):
            # 这个地方一定要注意不是length+1
            # 要看dp[i]中i的含义为下标
            dp[i]=max(dp[i-1],dp[i-2]+nums[i])
        return dp[-1]
# @lc code=end
'''
dp[i]：考虑下标i（包括i）以内的房屋，最多可以偷窃的金额为dp[i]。
'''
