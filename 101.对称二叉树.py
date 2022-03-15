#
# @lc app=leetcode.cn id=101 lang=python3
#
# [101] 对称二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        def dfs(leftnode,rightnode):
            if not leftnode and not rightnode:
                return True
            elif not leftnode or not rightnode:
                return False
            elif leftnode.val!=rightnode.val:
                return False
            else:
                return dfs(leftnode.left,rightnode.right) and dfs(rightnode.left,leftnode.right)

        return dfs(root.left,root.right)
# @lc code=end

'''
https://leetcode-cn.com/problems/symmetric-tree/solution/pythonpython3di-fa-dfs-by-null-o38-yy5y/
深度优先，需要注意的是轴对称，随意左边的左相当于右边的右
'''