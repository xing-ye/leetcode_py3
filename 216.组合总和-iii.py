#
# @lc app=leetcode.cn id=216 lang=python3
#
# [216] 组合总和 III
#

# @lc code=start
class Solution:
    def __init__(self) -> None:
        self.sum=0
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res=[]
        path=[]
        def backtrace(startIdx,k,n):
            if self.sum>n:#第一次剪枝
                return 
            if len(path)==k:
                if self.sum==n:
                    res.append(path[:])
                    return 
            for i in range(startIdx,9-(k-len(path))+2):
                path.append(i)
                self.sum+=i
                backtrace(i+1,k,n)
                path.pop()
                self.sum-=i
        backtrace(1,k,n)
        return res
# @lc code=end
'''
类似于第77题，不同的是在77中n是数的范围，而这里是和为n的结果，
所以在剪枝时，要换成9，并且在剪枝时还要多一个判断是否和大于n的判断
具体的可以去看77结合理解


'''
