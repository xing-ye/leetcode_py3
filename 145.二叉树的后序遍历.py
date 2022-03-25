#
# @lc app=leetcode.cn id=145 lang=python3
#
# [145] 二叉树的后序遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    #递归后序遍历
    def postorder(self,root: TreeNode,res):
        if root==None:
            return res       
        self.postorder(root.left, res)
        self.postorder(root.right, res)
        res.append(root.val)

    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        self.postorder(root, res)
        return res
# @lc code=end

