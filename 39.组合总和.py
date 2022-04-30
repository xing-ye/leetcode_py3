#
# @lc app=leetcode.cn id=39 lang=python3
#
# [39] 组合总和
#

# @lc code=start
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        path=[]
        result=[]
        candidates.sort()
        def backtrace(candidates,target,sum_num,startIdx):
            if sum_num==target:
                result.append(path[:])
                return 

            for i in range(startIdx,len(candidates)):

                if sum_num+candidates[i]>target:#剪枝
                    return 
                sum_num+=candidates[i]
                path.append(candidates[i])
                backtrace(candidates,target,sum_num,i)
                #因为已经排序过，所以只用控制i就可以控制选择了，
                # 并且因为可以无限重复选择，所以还是从i开始
                sum_num-=candidates[i]# 回溯
                path.pop()# 回溯

        backtrace(candidates,target,0,0)
        return result
            

# @lc code=end

