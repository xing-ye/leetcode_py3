#
# @lc app=leetcode.cn id=746 lang=python3
#
# [746] 使用最小花费爬楼梯
#

# @lc code=start
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp=[0]*(len(cost))
        # 用dp保存路程的总花费
        dp[0]=cost[0]
        dp[1]=cost[1]
        for i in range(2,len(cost)):
            # 我们要爬到最顶端，实际上就是cost数组外的第一个。
            # 所以实际上是计算到cost+1个台阶的值，因为最后一层不算
            # 所以实际上就是p[len(cost)-1],dp[len(cost)-2]的值
            dp[i]=min(dp[i-1],dp[i-2])+cost[i]
        return min(dp[len(cost)-1],dp[len(cost)-2])
# @lc code=end
'''
# dp[i] = min(dp[i - 1], dp[i - 2]) + cost[i]
从例子里可以看到，其实最后一步没有算cost
'''