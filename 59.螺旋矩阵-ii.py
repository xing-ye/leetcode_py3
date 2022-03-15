#
# @lc app=leetcode.cn id=59 lang=python3
#
# [59] 螺旋矩阵 II
#

# @lc code=start
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix=[[0]*n for _ in range(n)]# 创建n*n矩阵
        left,right,up,down=0,n-1,0,n-1
        number=1#要填充的数字
        '''
        这四个分别用来控制操作的范围，遵循左闭右开的原则进行操作
        比如第一行只操作1、2，然后按列操作3、4，再按行5、6以此类推
        需要牢记，这种需要做多个类似操作的(比图二分查找等)
        最重要的就是找到一个统一的操作规则，详见：
        https://programmercarl.com/0059.%E8%9E%BA%E6%97%8B%E7%9F%A9%E9%98%B5II.html#%E6%80%9D%E8%B7%AF
        '''
        if n==1:
            matrix[0][0]=1
            return matrix
        while left<right and up<down:
            #从左到右填充
            for x in range(left,right):
                matrix[up][x]=number
                number+=1
            
            #从上到下
            for y in range(up,down):
                matrix[y][right]=number
                number+=1
            
            # 从右到左
            for x in range(right,left,-1):
                matrix[down][x]=number
                number+=1
            
            #从下到上
            for y in range(down,up,-1):
                matrix[y][left]=number
                number+=1
            #更新边界
            left+=1
            right-=1
            up+=1
            down-=1
            #如果阶数为奇数，额外填充一次中心
            if n%2:
                matrix[n//2][n//2]=number
        
        return matrix

# @lc code=end

