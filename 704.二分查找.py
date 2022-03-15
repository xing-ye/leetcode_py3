#
# @lc app=leetcode.cn id=704 lang=python3
#
# [704] 二分查找
#

# @lc code=start
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left,right=0,len(nums)-1
        # 选用两边闭的区间[left,right]
        while left<=right:
            middle=left+(right-left)//2
            if nums[middle]==target:
                return middle
            elif nums[middle]>target:
                right=middle-1
            elif nums[middle]<target:
                left=middle+1
        return -1

# @lc code=end

