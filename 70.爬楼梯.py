#
# @lc app=leetcode.cn id=70 lang=python3
#
# [70] 爬楼梯
#

# @lc code=start
class Solution:
    def climbStairs(self, n: int) -> int:
        # 动态规划
        fir=1#初始化跳到第一层和第二层的方法
        sec=2#调到第二层有两种方法
        tmp=0
        if n<3:
            return n
        for i in range(3,n+1):
            # dp[i]=dp[i-1]+dp[i-2]
            # 空间复杂度为O（n）
            tmp=fir+sec
            fir=sec
            sec=tmp
            
        return sec
# @lc code=end
'''
存储的是跳到n层所有可能的跳数。
动态规划方法:跳到第三层的方法实际上就是跳到第一层和第二层的方法的和，即dp[i]=dp[i-1]+dp[i-2]
因为每次最多走1步或两步。
'''
