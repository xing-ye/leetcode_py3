#
# @lc app=leetcode.cn id=530 lang=python3
#
# [530] 二叉搜索树的最小绝对差
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
        '''
        迭代，先中序遍历，将搜索树转换为数组，在进行查找
        '''
        cha=float("inf")
        res=[]
        res=self.transfer(root,res)
        for i in range(len(res)-1):
            cha=min(abs(res[i]-res[i+1]),cha)
        return cha


    
    def transfer(self,root,res):
        if not root:
            return None
        if root.left:
            self.transfer(root.left,res)
        res.append(root.val)
        if root.right:
            self.transfer(root.right,res)
        return res
# @lc code=end

