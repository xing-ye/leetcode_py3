#
# @lc app=leetcode.cn id=131 lang=python3
#
# [131] 分割回文串
#

# @lc code=start
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result=[]
        path=[]

        def backtrace(s,startIdx):
            if startIdx>=len(s):
                result.append(path[:])
                return
            for i in range(startIdx,len(s)):
                tmp=s[startIdx:i+1]#这也是左闭右开的吗，所以不会溢出
                if tmp==tmp[::-1]:
                    path.append(tmp)
                    backtrace(s,i+1)
                    path.pop()
                else:
                    continue
        backtrace(s,0)
        return result

# @lc code=end

