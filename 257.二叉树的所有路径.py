#
# @lc app=leetcode.cn id=257 lang=python3
#
# [257] 二叉树的所有路径
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    '''
    递归的方式，实际上是一种隐形的回溯
    https://programmercarl.com/0257.%E4%BA%8C%E5%8F%89%E6%A0%91%E7%9A%84%E6%89%80%E6%9C%89%E8%B7%AF%E5%BE%84.html#%E8%BF%AD%E4%BB%A3%E6%B3%95
    '''
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        path=''
        res=[]
        if not root:
            return res
        self.traversal(root,path,res)
        return res
        
    def traversal(self,cur,path,result):
        path+=str(cur.val)
        if not cur.left and not cur.right:
            result.append(path)
        if cur.left:
            self.traversal(cur.left,path+'->',result)
        if cur.right:
            self.traversal(cur.right,path+'->',result)
        

# @lc code=end

