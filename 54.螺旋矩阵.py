#
# @lc app=leetcode.cn id=54 lang=python3
#
# [54] 螺旋矩阵
#

# @lc code=start


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m=len(matrix)#行数
        n=len(matrix[0])#列数
        length=n*m
        res=[0]*length 
        left,right,up,down=0,n-1,0,m-1
        number=0#控制res坐标
        '''
        这四个分别用来控制操作的范围，遵循左闭右开的原则进行操作
        要注意这里不是方阵二是矩阵，所以会和59有很大区别
        最重要的就是找到一个统一的操作规则，详见：
        https://programmercarl.com/0059.%E8%9E%BA%E6%97%8B%E7%9F%A9%E9%98%B5II.html#%E6%80%9D%E8%B7%AF
        '''
        if n==1:
            for i in range(0,m):
                res[number]=matrix[i][0]
                number+=1
            return res
        if m==1:
            for i in range(0,n):
                res[number]=matrix[0][i]
                number+=1
            return res        
        while left<right and up<down:
            #从左到右填充
            for x in range(left,right):
                res[number]= matrix[up][x]
                number+=1
            
            #从上到下
            for y in range(up,down):
                res[number]=matrix[y][right]
                number+=1
            
            # 从右到左
            for x in range(right,left,-1):
                res[number]=matrix[down][x]
                number+=1
            
            #从下到上
            for y in range(down,up,-1):
                res[number]=matrix[y][left]
                number+=1
            #更新边界
            left+=1
            right-=1
            up+=1
            down-=1
            #如果阶数为奇数，额外填充一次中心
            if left==right:
                for i in range(up,down+1):
                    res[number]=matrix[i][left]
                    number+=1
                break
            if up==down:
                for i in range(left,right+1):
                    res[number]=matrix[up][i]
                    number+=1
                break

            
        return res

# @lc code=end

