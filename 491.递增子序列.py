#
# @lc app=leetcode.cn id=491 lang=python3
#
# [491] 递增子序列
#

# @lc code=start
class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        res=[]
        path=[]
        def backtracking(nums,start_index):
             # 收集结果，同78.子集，仍要置于终止条件之前
            if len(path) >= 2:
                # 本题要求所有的节点
                res.append(path[:])
        
            # Base Case（可忽略）
            if start_index == len(nums):
                return

            # 单层递归逻辑
            # 深度遍历中每一层都会有一个全新的usage_list用于记录本层元素是否重复使用
            usage_list = set()
            # 同层横向遍历
            for i in range(start_index, len(nums)):
                # 若当前元素值小于前一个时（非递增）或者曾用过，跳入下一循环
                if (path and nums[i] < path[-1]) or nums[i] in usage_list:
                    continue
                usage_list.add(nums[i])
                path.append(nums[i])
                backtracking(nums, i+1)
                path.pop() 
        backtracking(nums,0)
        return res

# @lc code=end

