#
# @lc app=leetcode.cn id=977 lang=python3
#
# [977] 有序数组的平方
#

# @lc code=start
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        '''
        采用双指针法，可以实现时间复杂度O(n)的效果
        '''
        if len(nums)==1:
            return [nums[0]*nums[0]]
        left,right=0,len(nums)-1
        res=[-1]*len(nums)#用来存放结果
        idx=len(nums)-1
        while left<=right:
            if nums[left]*nums[left]<nums[right]*nums[right]:
                res[idx]=nums[right]*nums[right]
                right-=1
            else:
                res[idx]=nums[left]*nums[left]
                left+=1
            idx-=1
        return res
# @lc code=end

