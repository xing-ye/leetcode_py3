#
# @lc app=leetcode.cn id=1 lang=python3
#
# [1] 两数之和
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        record=dict()
        for idx,value in enumerate(nums):
            if target-value not in record:
                record[value]=idx
            else:
                return [record[target-value],idx]
#题目说明每种输入只会对应一个答案所以只要有就可以返回了

# @lc code=end

'''
本题同样是hash的思想，但是使用dict作为媒介

数组的大小是受限制的，而且如果元素很少，而哈希值太大会造成内存空间的浪费。
set是一个集合，里面放的元素只能是一个key，而两数之和这道题目，
不仅要判断y是否存在而且还要记录y的下标位置，因为要返回x 和 y的下标。
所以set 也不能用。这里用dict
'''