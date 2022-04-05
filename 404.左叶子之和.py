#
# @lc app=leetcode.cn id=404 lang=python3
#
# [404] 左叶子之和
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque


class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        stack=deque()
        res=0
        stack.append(root)
        while stack:
            node=stack.popleft()
            if node.left and not node.left.left and not node.left.right:
                res+=node.left.val
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        return res
# @lc code=end

