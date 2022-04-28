#
# @lc app=leetcode.cn id=40 lang=python3
#
# [40] 组合总和 II
#

# @lc code=start
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result=[]
        path=[]
        used=[False]*len(candidates)#记录是否使用过，没使用为false
        # 必须提前进行数组排序，避免重复
        candidates.sort()
        def backtrace(candidates,target,statIdx,sum):
            if sum==target:
                result.append(path[:])
                return
            for i in range(statIdx,len(candidates)):
                if sum+candidates[i]>target:
                    return
                if i>0 and candidates[i]==candidates[i-1] and used[i-1]==False:
                    continue
                '''
                如果前一个为false并且与前一个相同，表明在同一层使用过
                而若为true则说明在这一支琏用过了，具体看代码随想录
                '''
                sum+=candidates[i]
                path.append(candidates[i])
                used[i]=True
                backtrace(candidates,target,i+1,sum)#因为要求不能重复，所以从i+1开始
                sum-=candidates[i]
                path.pop()
                used[i]=False

        backtrace(candidates,target,0,0)

        return result
# @lc code=end
'''
https://programmercarl.com/0040.%E7%BB%84%E5%90%88%E6%80%BB%E5%92%8CII.html#python
'''

