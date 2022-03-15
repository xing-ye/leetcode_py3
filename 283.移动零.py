#
# @lc app=leetcode.cn id=283 lang=python3
#
# [283] 移动零
#

# @lc code=start
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        实际上还是采用快慢指针的思路
        """
        slowIdx=0
        for fastIdx in range(len(nums)):
            if nums[fastIdx]!=0:
                nums[slowIdx]=nums[fastIdx]
                slowIdx+=1
        for fastIdx in range(slowIdx,len(nums)):
            nums[fastIdx]=0
# @lc code=end

