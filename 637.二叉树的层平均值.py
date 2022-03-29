#
# @lc app=leetcode.cn id=637 lang=python3
#
# [637] 二叉树的层平均值
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
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        if not root:
            return []
        res=[]
        que=deque([root])
        #对于一个treenode并不是可迭代的，需要存入[]中才行
        while que:
            size=len(que)
            tmp=[]
            sum=0
            for _ in range(size):
                node=que.popleft()
                sum+=node.val
                if node.left:
                    que.append(node.left)
                if node.right:
                    que.append(node.right)
            res.append(sum/size)
        return res

# @lc code=end

