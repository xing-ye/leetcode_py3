#
# @lc app=leetcode.cn id=96 lang=python3
#
# [96] 不同的二叉搜索树
#

# @lc code=start
class Solution:
    def numTrees(self, n: int) -> int:
        dp=[0]*(n+1)
        dp[0]=dp[1]=1# 无节点的dp[0]也算一个二叉树
        for i in range(2,n+1):
            for j in range(1,i+1):
                dp[i]+=dp[j-1]*dp[i-j]
        return dp[n]
# @lc code=end
'''
# 动态规划
dp[i]=dp[j-1]*dp[i-j]
这里的j是指1到i的遍历，dp[i]代表有i个节点组成的二叉搜索树的数目，要注意dp[i]是指有1、2、3....、i组成的i个节点
所以，以J为节点，那么一定有j-1个小于j，在j的左子树
有i-j个大于j在右子树

'''
