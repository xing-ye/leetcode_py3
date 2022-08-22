#
# @lc app=leetcode.cn id=1035 lang=python3
#
# [1035] 不相交的线
#

# @lc code=start
class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        len1,len2=len(nums1),len(nums2)
        dp=[[0]*(len2+1) for _ in range(len1+1)]
        for i in range(1,len1+1):
            for j in range(1,len2+1):
                if nums1[i-1]==nums2[j-1]:
                    dp[i][j]=dp[i-1][j-1]+1
                else:
                    dp[i][j]=max(dp[i-1][j],dp[i][j-1])

        return dp[-1][-1]
# @lc code=end
'''
直线不能相交，这就是说明在字符串A中 找到一个与字符串B相同的子序列，且这个子序列不能改变相对顺序，只要相对顺序不改变，链接相同数字的直线就不会相交。

：本题说是求绘制的最大连线数，其实就是求两个字符串的最长公共子序列的长度！

dp[i][j]：长度为[0, i - 1]的字符串text1与长度为[0, j - 1]的字符串text2的最长公共子序列为dp[i][j]

如果text1[i - 1] 与 text2[j - 1]不相同，那就看看text1[0, i - 2]与text2[0, j - 1]的最长公共子序列 和 text1[0, i - 1]与text2[0, j - 2]的最长公共子序列，取最大的。

即：dp[i][j] = max(dp[i - 1][j], dp[i][j - 1]);
'''
