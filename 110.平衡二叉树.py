#
# @lc app=leetcode.cn id=110 lang=python3
#
# [110] 平衡二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        return self.check(root)!= -1
    def check(self,root):
        if not root:
            return 0
        leftHigh=self.check(root.left)
        if leftHigh==-1:
            return -1
        rightHigh=self.check(root.right)
        if rightHigh==-1:
            return -1
        return max(rightHigh,leftHigh)+1 if abs(leftHigh-rightHigh)<2 else -1


# @lc code=end
'''
想看此教程：
https://leetcode-cn.com/problems/balanced-binary-tree/solution/balanced-binary-tree-di-gui-fang-fa-by-jin40789108/
'''

