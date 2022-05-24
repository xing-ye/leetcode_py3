#
# @lc app=leetcode.cn id=78 lang=python3
#
# [78] 子集
#

# @lc code=start
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res=[]
        path=[]

        def backtracking(nums,startIdx):
            res.append(path[:])#保存所有路径
            if startIdx==len(nums):
                return
            for i in range(startIdx,len(nums)):
                path.append(nums[i])
                backtracking(nums,i+1)
                path.pop()
        backtracking(nums,0)
        return res

# @lc code=end
'''
要注意这个和77的不同，这个相当于把所有节点也都要保存，而77只是统计叶节点
https://programmercarl.com/0078.%E5%AD%90%E9%9B%86.html#python
'''
