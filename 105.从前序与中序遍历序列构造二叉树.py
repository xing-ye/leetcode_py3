#
# @lc app=leetcode.cn id=105 lang=python3
#
# [105] 从前序与中序遍历序列构造二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not preorder:
            return None
        value=preorder[0]
        root=TreeNode(value)
        separate_idx=inorder.index(value)
        inorder_left=inorder[:separate_idx]
        inorder_right=inorder[separate_idx+1:]
        preorder_left=preorder[1:1 + len(inorder_left)]
        preorder_right=preorder[1 + len(inorder_left):]
        root.left=self.buildTree(preorder_left,inorder_left)
        root.right=self.buildTree(preorder_right,inorder_right)

        return root
'''
https://programmercarl.com/0106.%E4%BB%8E%E4%B8%AD%E5%BA%8F%E4%B8%8E%E5%90%8E%E5%BA%8F%E9%81%8D%E5%8E%86%E5%BA%8F%E5%88%97%E6%9E%84%E9%80%A0%E4%BA%8C%E5%8F%89%E6%A0%91.html#python
'''

# @lc code=end

