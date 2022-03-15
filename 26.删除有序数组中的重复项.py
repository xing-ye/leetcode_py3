#
# @lc app=leetcode.cn id=26 lang=python3
#
# [26] 删除有序数组中的重复项
#

# @lc code=start
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        slowIdx=0
        for fastIdx in range(len(nums)):
            if nums[fastIdx]!=nums[slowIdx]:
                slowIdx+=1
                nums[slowIdx]=nums[fastIdx]
                
        return slowIdx+1      
# @lc code=end
'''
这里同样是采用快慢指针的方式，但是要注意与27题的区别
这里是你要比较的是相邻的数组，若两者不相同，你是需要先保存自己的内容的
而27是比较一个确定的数，只要不同就保存就可
要好好体会一下
'''
