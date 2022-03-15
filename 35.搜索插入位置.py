#
# @lc app=leetcode.cn id=35 lang=python3
#
# [35] 搜索插入位置
#

# @lc code=start
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left,right=0,len(nums)-1
        while left<=right:
            middle=left+(right-left)//2
            if nums[middle]==target:
                return middle
            elif nums[middle]>target:
                right=middle-1
            elif nums[middle]<target:
                left=middle+1
           # if left==right:
            #    return left
        return left #也可以返回right+1
# @lc code=end

'''
对于闭的区间，推出循环的条件是right<left，
而此时重要的就是选择一个合适的能够表示插入位置的left或right式子即可
可以画图来确定
'''