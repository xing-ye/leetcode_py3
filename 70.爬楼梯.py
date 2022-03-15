#
# @lc app=leetcode.cn id=70 lang=python3
#
# [70] 爬楼梯
#

# @lc code=start
class Solution:
    def climbStairs(self, n: int) -> int:
        dp=[0]*(n+1)#这里是n+1是因为还有0
        dp[0]=dp[1]=1
        for i in range(2,n+1):
            dp[i]=dp[i-1]+dp[i-2]
            
        return dp[-1]
# @lc code=end
'''
dp[n]存储的是跳到n层所有可能的跳数。
详见：
https://leetcode-cn.com/problems/climbing-stairs/solution/zhi-xin-hua-shi-pa-lou-ti-zhi-cong-bao-l-lo1t/
'''
