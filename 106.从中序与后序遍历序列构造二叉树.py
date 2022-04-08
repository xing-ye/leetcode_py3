#
# @lc app=leetcode.cn id=106 lang=python3
#
# [106] 从中序与后序遍历序列构造二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        if not postorder:
            return None
        value=postorder[-1]
        root=TreeNode(value)
        separate_idx=inorder.index(value)
        inorder_left=inorder[:separate_idx]
        inorder_right=inorder[separate_idx+1:]
        postorder_left=postorder[:len(inorder_left)]
        postorder_right=postorder[len(inorder_left): len(postorder) - 1]
        root.left=self.buildTree(inorder_left,postorder_left)
        root.right=self.buildTree(inorder_right,postorder_right)

        return root
# @lc code=end

'''
https://programmercarl.com/0106.%E4%BB%8E%E4%B8%AD%E5%BA%8F%E4%B8%8E%E5%90%8E%E5%BA%8F%E9%81%8D%E5%8E%86%E5%BA%8F%E5%88%97%E6%9E%84%E9%80%A0%E4%BA%8C%E5%8F%89%E6%A0%91.html#python
'''