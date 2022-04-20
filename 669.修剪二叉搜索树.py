#
# @lc app=leetcode.cn id=669 lang=python3
#
# [669] 修剪二叉搜索树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
        if not root:
            return None
        if root.val<low:
            return self.trimBST(root.right,low,high)
        if root.val>high:
            return self.trimBST(root.left,low,high)
        if root.val>=low and root.val<=high:
            root.left = self.trimBST(root.left, low, high)
            root.right = self.trimBST(root.right, low, high)
            return root
# @lc code=end
'''
上面操作类似于删除搜索二叉树得节点，未操作得就被删除了。
要注意if判断得边界不要有重合
'''
