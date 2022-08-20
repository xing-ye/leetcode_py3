#
# @lc app=leetcode.cn id=1143 lang=python3
#
# [1143] 最长公共子序列
#

# @lc code=start
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        len1,len2=len(text1),len(text2)
        if len1==0 or len2==0:
            return 0
        dp=[[0]*(len2+1) for _ in range(len1+1)]
        # len1+1行，len2+1列
        for i in range(1,len1+1):
            for j in range(1,len2+1):
                if text1[i-1]==text2[j-1]:
                    dp[i][j]=dp[i-1][j-1]+1
                else:
                    dp[i][j]=max(dp[i-1][j],dp[i][j-1])

        return dp[-1][-1]
# @lc code=end
'''
dp[i][j]：长度为[0, i - 1]的字符串text1与长度为[0, j - 1]的字符串text2的最长公共子序列为dp[i][j]

text1[i - 1] 与 text2[j - 1]相同，那么找到了一个公共元素，所以dp[i][j] = dp[i - 1][j - 1] + 1;
如果text1[i - 1] 与 text2[j - 1]不相同，那就看看text1[0, i - 2]与text2[0, j - 1]的最长公共子序列 和 text1[0, i - 1]与text2[0, j - 2]的最长公共子序列，取最大的。
即：dp[i][j] = max(dp[i - 1][j], dp[i][j - 1]);

初始化：dp[i][0] = 0;dp[0][j]也是0
'''