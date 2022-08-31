#
# @lc app=leetcode.cn id=516 lang=python3
#
# [516] 最长回文子序列
#

# @lc code=start
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        len1=len(s)
        dp=[[0]*len1 for _ in range(len1)]
        for i in range(len1):
            dp[i][i]=1
        for i in range(len1-1,-1,-1):
            for j in range(i+1,len1):
                # 这里+1是为了避免j=0，并且需要相同的已经初始化了，所以不不需要i与j相同，否则下面的就不该是+2了。
                if s[i]==s[j]:
                    dp[i][j]=dp[i+1][j-1]+2
                else:
                    dp[i][j]=max(dp[i+1][j],dp[i][j-1])
                    
        return dp[0][-1]
# @lc code=end

'''
要注意回文子串是要连续的，回文子序列可不是连续的！

dp[i][j]：字符串s在[i, j]范围内最长的回文子序列的长度为dp[i][j]。

在判断回文子串的题目中，关键逻辑就是看s[i]与s[j]是否相同。

如果s[i]与s[j]相同，那么dp[i][j] = dp[i + 1][j - 1] + 2;

如果s[i]与s[j]不相同，说明s[i]和s[j]的同时加入 并不能增加[i,j]区间回文子串的长度，那么分别加入s[i]、s[j]看看哪一个可以组成最长的回文子序列。

加入s[j]的回文子序列长度为dp[i + 1][j]。

加入s[i]的回文子序列长度为dp[i][j - 1]。

那么dp[i][j]一定是取最大的，即：dp[i][j] = max(dp[i + 1][j], dp[i][j - 1]);

初始化：对角线为1

遍历顺序：根据dp[i][j] = dp[i + 1][j - 1] + 2;需要从下到上，从左到右
'''