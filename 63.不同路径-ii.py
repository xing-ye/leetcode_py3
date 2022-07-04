#
# @lc app=leetcode.cn id=63 lang=python3
#
# [63] 不同路径 II
#

# @lc code=start
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        row,column=len(obstacleGrid),len(obstacleGrid[0])
        # 获取行和列
        dp=[[0 for _ in range(column)] for _ in range(row)]
        for i in range(column):
            # 处理第一行
            if obstacleGrid[0][i]==1:break
            dp[0][i]=1
        for i in range(row):
            # 处理第一列
            if obstacleGrid[i][0]==1:break
            dp[i][0]=1
        for i in range(1,row):
            for j in range(1,column):
                if obstacleGrid[i][j]==1:continue
                dp[i][j]=dp[i-1][j]+dp[i][j-1]
        return dp[-1][-1]
# @lc code=end
'''
dp的设置与62同存储的是到该点的路径数，需要注意在计算前需要判断障碍
'''
