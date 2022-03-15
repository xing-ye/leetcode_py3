#
# @lc app=leetcode.cn id=844 lang=python3
#
# [844] 比较含退格的字符串
#

# @lc code=start
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        '''
        很关键的一个思想就是从后向前进行判断，这样就节省了判断所需的资源
        同样采用快慢指针的情况，参考自：
        https://leetcode-cn.com/problems/backspace-string-compare/solution/shuang-zhi-zhen-bi-jiao-han-tui-ge-de-zi-8fn8/

        '''
        i, j = len(s) - 1, len(t) - 1
        skipS = skipT = 0

        while i >= 0 or j >= 0:
            while i >= 0:#用来处理skipS
                if s[i] == "#":
                    skipS += 1
                    i -= 1
                elif skipS > 0:
                    skipS -= 1
                    i -= 1
                else:
                    break
            while j >= 0:
                if t[j] == "#":
                    skipT += 1
                    j -= 1
                elif skipT > 0:
                    skipT -= 1
                    j -= 1
                else:
                    break
            if i >= 0 and j >= 0:
                if s[i] != t[j]:
                    return False
            elif i >= 0 or j >= 0:
                return False
            i -= 1
            j -= 1
        
        return True

# @lc code=end

