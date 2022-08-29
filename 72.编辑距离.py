#
# @lc app=leetcode.cn id=72 lang=python3
#
# [72] 编辑距离
#

# @lc code=start
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        len1,len2=len(word1)+1,len(word2)+1
        dp=[[0]*len2 for _ in range(len1)]
        for i in range(len1):
            dp[i][0]=i
        for j in range(len2):
            dp[0][j]=j
        for i in range(1,len1):
            for j in range(1,len2):
                if word1[i-1]==word2[j-1]:
                    dp[i][j]=dp[i-1][j-1]
                else:
                    dp[i][j]=min(dp[i-1][j-1],dp[i][j-1],dp[i-1][j])+1

        return dp[-1][-1]
# @lc code=end

'''
要注意dp只是描述一种状态的转移，并不是真的去操作了
dp[i][j] 表示以下标i-1为结尾的字符串word1，和以下标j-1为结尾的字符串word2，最近编辑距离为dp[i][j]。

if (word1[i - 1] == word2[j - 1]) 那么说明不用任何编辑，dp[i][j] 就应该是 dp[i - 1][j - 1]，即dp[i][j] = dp[i - 1][j - 1];

if (word1[i - 1] != word2[j - 1])，此时就需要编辑了，如何编辑呢？

操作一：word1删除一个元素，那么就是以下标i - 2为结尾的word1 与 j-1为结尾的word2的最近编辑距离 再加上一个操作。
即 dp[i][j] = dp[i - 1][j] + 1;

操作二：word2删除一个元素，那么就是以下标i - 1为结尾的word1 与 j-2为结尾的word2的最近编辑距离 再加上一个操作。
即 dp[i][j] = dp[i][j - 1] + 1;

word2添加一个元素，相当于word1删除一个元素，

操作三：替换元素，word1替换word1[i - 1]，使其与word2[j - 1]相同，此时不用增加元素，那么以下标i-2为结尾的word1 与 j-2为结尾的word2的最近编辑距离 加上一个替换元素的操作。

即 dp[i][j] = dp[i - 1][j - 1] + 1;

初始化：dp[i][0]=i,dp[0][j]=j
'''