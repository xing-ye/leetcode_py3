#
# @lc app=leetcode.cn id=27 lang=python3
#
# [27] 移除元素
#

# @lc code=start
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        slowIdx=0
        for fastIdx in range(len(nums)):
            if nums[fastIdx]!=val:
                nums[slowIdx]=nums[fastIdx]
                slowIdx+=1
        return slowIdx
# @lc code=end
'''
主要要学会的是两个快慢指针的方式来删除元素
空间占用率O(1)
时间占用率O(n)
'''
