#
# @lc app=leetcode.cn id=47 lang=python3
#
# [47] 全排列 II
#

# @lc code=start
from re import T


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res=[]
        path=[]
        nums.sort()#要先排序，因为给的不一定是排序的否则无法去同一层的重
        used=[False]*len(nums)
        def backtracking(nums,used):
            if len(nums)==len(path):
                res.append(path[:])
                return 
            # 这里也不需要有staridx，针对排列
            for i in range(len(nums)):
                if used[i]==True:
                    continue
                if i>0 and nums[i]==nums[i-1] and not used[i-1]:
                    continue
                used[i]=True
                path.append(nums[i])
                backtracking(nums,used)
                path.pop()
                used[i]=False
        backtracking(nums,used)
        return res
# @lc code=end
'''
要注意的是同一层不可以相同，那么应该是used[i-1]为false
因为一次回溯实际上是往深度去走，所以如果为true是判断不能有重复元素
'''
