#
# @lc app=leetcode.cn id=226 lang=python3
#
# [226] 翻转二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import collections
class Solution:
    # 层序遍历
    def invertTree(self, root: TreeNode) -> TreeNode:
        queue = collections.deque() #使用deque()
        if root:
            queue.append(root)
        while queue:
            size = len(queue)
            for i in range(size):
                node = queue.popleft()
                node.left, node.right = node.right, node.left #节点处理
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return root
# @lc code=end

'''
递归：
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return None
        root.left,root.right=root.right,root.left
        self.invertTree(root.left)
        self.invertTree(root.right)       
        return root
'''
'''
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return root
        st = []
        st.append(root)
        while st:
            node = st.pop()
            node.left, node.right = node.right, node.left #中
            if node.right:
                st.append(node.right) #右
            if node.left:
                st.append(node.left) #左
        return root
'''