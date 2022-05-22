#
# @lc app=leetcode.cn id=37 lang=python3
#
# [37] 解数独
#

# @lc code=start

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def isvalid(row,col,val,board):
            for i in range(len(board)):#hang
                if board[i][col]==val:
                    return False
            for i in range(len(board[0])):#lie
                if board[row][i]==val:
                    return False
            startRow=(row//3)*3 #row所在小矩阵的起始位置
            startCol=(col//3)*3
            for i in range(startRow,startRow+3):#左闭右开
                for j in range(startCol,startCol+3):
                    if board[i][j]==val:
                        return False
            return True

        def backtracking(board):
            for i in range(len(board)):
                for j in range(len(board[0])):
                    if board[i][j]!='.':
                        continue
                    for k in range(1,10):
                        if isvalid(i,j,str(k),board):
                            board[i][j]=str(k)
                            if backtracking(board): return True
                            # 如果可以填完就直接返回了，不用在后续继续回溯了
                            board[i][j]='.'
                    return False #如果9个数都不行
            return True #都填上了，回溯结束

        backtracking(board)



# @lc code=end

