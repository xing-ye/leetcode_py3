#
# @lc app=leetcode.cn id=90 lang=python3
#
# [90] 子集 II
#

# @lc code=start
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res=[]
        path=[]
        nums.sort()#注意要排序

        def backtracking(nums,startIdx):
            res.append(path[:])#空集也包括
            if startIdx==len(nums):
                return 
            for i in range (startIdx,len(nums)):
                if i>startIdx and nums[i]==nums[i-1]:
                    continue
                path.append(nums[i])
                backtracking(nums,i+1)
                path.pop()
        backtracking(nums,0)
        return res
# @lc code=end

'''
与78相比，要排除同一层中重复的元素。因为是res中不能有重复的
如要求path中不能重复，那么也要处理同一支链也不能重复
'''