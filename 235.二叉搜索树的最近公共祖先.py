#
# @lc app=leetcode.cn id=235 lang=python3
#
# [235] 二叉搜索树的最近公共祖先
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
        if root.val>p.val and root.val>q.val:
            return self.lowestCommonAncestor(root.left,p,q)
        if root.val<p.val and root.val<q.val:
            return self.lowestCommonAncestor(root.right,p,q)
        return root
        
# @lc code=end
'''
我们知道搜索树是有大小关系的
所以，如果root的值正好在p和q之间那么就是公共祖先
并且，使用后续遍历，即可获得最小的，
'''
