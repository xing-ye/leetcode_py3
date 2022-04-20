#
# @lc app=leetcode.cn id=236 lang=python3
#
# [236] 二叉树的最近公共祖先
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        '''
        主要做查询p和q的操作，只有找到节点才会返回一个节点
        其余都是返回空，这样左右两个都不为空的就是共同最小祖先节点
        '''
        if not root or root==p or root==q:
            return root
        left=self.lowestCommonAncestor(root.left,p,q)
        right=self.lowestCommonAncestor(root.right,p,q)

        if left and right:
            return root
        if left:
            return left

        return right #对于其他情况都返回right即可，为空其实就是None
# @lc code=end
'''
必须使用后序遍历，这样才能够处理好两个节点的结果
具体看随想录
'''
