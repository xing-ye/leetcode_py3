#
# @lc app=leetcode.cn id=343 lang=python3
#
# [343] 整数拆分
#

# @lc code=start
class Solution:
    def integerBreak(self, n: int) -> int:
        dp=[0]*(n+1)
        # 这里是n+1，因为dp[n]才表示到n的最大乘积
        dp[2]=1
        # 1*1=1。dp[0]和dp[1]没有必要初始化
        for i in range(3,n+1):
            for j in range(1,i-1):
                # 这里是因为划分出1或者0没有意义
                dp[i]=max(dp[i],(i-j)*j,j*dp[i-j])
        return dp[n]
# @lc code=end

# 动态规划，关键也是如何的定义dp
'''
定义dp[i]是分割i后的最大乘积
那么他们的关系应该是： dp[i] = max(dp[i], max(j * (i - j), j * dp[i - j]))
 假设对正整数 i 拆分出的第一个正整数是 j（1 <= j < i），则有以下两种方案：
# 1) 将 i 拆分成 j 和 i−j 的和，且 i−j 不再拆分成多个正整数，此时的乘积是 j * (i-j)
# 2) 将 i 拆分成 j 和 i−j 的和，且 i−j 继续拆分成多个正整数，此时的乘积是 j * dp[i-j]

'''