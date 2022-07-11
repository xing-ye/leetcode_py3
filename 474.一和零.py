#
# @lc app=leetcode.cn id=474 lang=python3
#
# [474] 一和零
#

# @lc code=start
class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        dp=[[0 for _ in range(n+1)] for _ in range(m+1)]
        # m+1行，n+1列，行m代表0个数，列n代表1的个数
        for str in strs:
            zeroNum=str.count('0')
            oneNum=str.count('1')
            # 从后往前遍历一直到dp[zeroNum][oneNum]
            # 从后往前遍历是因为，后面的是由前面的推到的，这样可以防止重复方如前面已经放入的物品
            for i in range(m,zeroNum-1,-1):
                for j in range(n,oneNum-1,-1):
                    dp[i][j]=max(dp[i][j],dp[i-zeroNum][j-oneNum]+1)
                    
        return dp[m][n]
# @lc code=end

'''
不是多重背包，要分清(见网站)
dp[i][j]：最多有i个0和j个1的strs的最大子集的大小为dp[i][j]。
dp[i][j] 可以由前一个strs里的字符串推导出来，strs里的字符串有zeroNum个0，oneNum个1。
dp[i][j] 就可以是 dp[i - zeroNum][j - oneNum] + 1。
dp[i][j] = max(dp[i][j], dp[i - zeroNum][j - oneNum] + 1);
这种用max的，dp的含义往往是求最大，而用相加的dp的意义往往代表种类

'''