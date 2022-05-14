#
# @lc app=leetcode.cn id=46 lang=python3
#
# [46] 全排列
#

# @lc code=start
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result =[]
        path =[]
        used=[False]*len(nums)

        def backtracing(nums,used):
            if len(path)==len(nums):
                result.append(path[:])
                return 
            for i in range(0,len(nums)):
                if used[i]==True:
                    continue
                used[i]=True
                path.append(nums[i])
                backtracing(nums,used)
                used[i]=False
                path.pop()
        backtracing(nums,used)

        return result
# @lc code=end

'''
排列问题的不同：
每层都是从0开始搜索而不是startIndex
需要used数组记录path里都放了哪些元素了
'''