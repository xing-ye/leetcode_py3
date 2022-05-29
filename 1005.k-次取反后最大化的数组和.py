#
# @lc app=leetcode.cn id=1005 lang=python3
#
# [1005] K 次取反后最大化的数组和
#

# @lc code=start
class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        nums=sorted(nums,key=abs,reverse=True)#将nums按照绝对值从大到小排序。
        for i in range (len(nums)):
            if k>0 and nums[i]<0:
                nums[i]*=-1
                k-=1
        if k%2==1:#最后一个为奇数时才需要变成负的，否则还是正
            nums[-1]*=-1
        return sum(nums)
# @lc code=end

