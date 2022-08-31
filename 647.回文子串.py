#
# @lc app=leetcode.cn id=647 lang=python3
#
# [647] 回文子串
#

# @lc code=start
class Solution:
    def countSubstrings(self, s: str) -> int:
        len1=len(s)
        dp=[[False]*len1 for _ in range(len1)]
        res=0
        for i in range(len1-1,-1,-1):
            for j in range(i,len1):
                # 这里不需要i+1开始，是因为只有当s[i]不等于s[j]时才会有j-1，所以不需要.而且这里求得是个数而不是一个字串，所以下标i可以与 j相同
                if s[i]==s[j]:
                    if j-i<=1:
                        res+=1
                        dp[i][j]=True
                    elif dp[i+1][j-1]==True:
                        res+=1
                        dp[i][j]=True
                # 对于不相等的不用处理，因为初始化就是false了
        return res
# @lc code=end

'''
布尔类型的dp[i][j]：表示区间范围[i,j] （注意是左闭右闭）的子串是否是回文子串，如果是dp[i][j]为true，否则为false。
当s[i]与s[j]不相等，那没啥好说的了，dp[i][j]一定是false。

当s[i]与s[j]相等时，这就复杂一些了，有如下三种情况

情况一：下标i 与 j相同，同一个字符例如a，当然是回文子串
情况二：下标i 与 j相差为1，例如aa，也是回文子串
情况三：下标：i 与 j相差大于1的时候，例如cabac，此时s[i]与s[j]已经相同了，我们看i到j区间是不是回文子串就看aba是不是回文就可以了，那么aba的区间就是 i+1 与 j-1区间，这个区间是不是回文就看dp[i + 1][j - 1]是否为true。

dp[i][j]初始化为false。

遍历顺序：由于情况3，一定要从下到上，从左到右遍历，这样保证dp[i + 1][j - 1]都是经过计算的。 其实就是类似于双指针从首尾向中间扫

'''