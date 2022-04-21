#
# @lc app=leetcode.cn id=701 lang=python3
#
# [701] 二叉搜索树中的插入操作
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        newNode=TreeNode(val)
        if not root:
            return newNode
        if not root.left and val<root.val:
            root.left=newNode
        if not root.right and val>root.val:
            root.right=newNode
        if val<root.val:
            self.insertIntoBST(root.left,val)
        if val >root.val:
            self.insertIntoBST(root.right,val)
        return root
# @lc code=end
'''
利用递归的方法
如果root为空则直接返回一个细节点，相当于创建
'''
