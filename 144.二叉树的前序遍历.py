#
# @lc app=leetcode.cn id=144 lang=python3
#
# [144] 二叉树的前序遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # 递归前序遍历函数
    def preOrder(self, root: TreeNode, res):
        if root == None:
            return res
        res.append(root.val)
        self.preOrder(root.left, res)
        self.preOrder(root.right, res)

    def preorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        self.preOrder(root, res)
        return res

# @lc code=end

