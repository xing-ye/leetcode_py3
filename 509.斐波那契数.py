#
# @lc app=leetcode.cn id=509 lang=python3
#
# [509] 斐波那契数
#

# @lc code=start
class Solution:
    def fib(self, n: int) -> int:
        if n<2:
            return n
        a,b,c=0,1,0
        for i in range(2,n+1):
            c=a+b
            a,b=b,c
        return c
# @lc code=end

