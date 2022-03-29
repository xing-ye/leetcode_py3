#
# @lc app=leetcode.cn id=104 lang=python3
#
# [104] 二叉树的最大深度
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # 广度优先遍历
        queue=[root]
        res=0
        if not root:
            return 0
        while queue:
            res+=1
            tmp=[]
            for node in queue:
                if node:
                    if node.left:
                        tmp.append(node.left)
                    if node.right:
                        tmp.append(node.right)
            queue=tmp#相比层序遍历，每次只存一层的数据

        return res
# @lc code=end

