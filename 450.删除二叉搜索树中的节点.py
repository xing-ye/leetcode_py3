#
# @lc app=leetcode.cn id=450 lang=python3
#
# [450] 删除二叉搜索树中的节点
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return root
        if root.val==key:
            if not root.left and not root.right:
                del root
                return None
            if not root.left and root.right:
                tmp=root
                root=root.right
                del tmp
                return root
            if  root.left and not root.right:
                tmp=root
                root=root.left
                del tmp
                return root
            if root.left and root.right:
                tmp=root
                v=root.right
                while v.left:
                    v=v.left
                v.left=root.left
                root=root.right
                del tmp
                return root
        if root.val>key:
            root.left=self.deleteNode(root.left,key)
        if root.val<key:
            root.right=self.deleteNode(root.right,key)
        return root

# @lc code=end
'''
要分情况处理，具体看下面的连接：
https://programmercarl.com/0450.%E5%88%A0%E9%99%A4%E4%BA%8C%E5%8F%89%E6%90%9C%E7%B4%A2%E6%A0%91%E4%B8%AD%E7%9A%84%E8%8A%82%E7%82%B9.html#java
'''
