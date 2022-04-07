#
# @lc app=leetcode.cn id=513 lang=python3
#
# [513] 找树左下角的值
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
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        '''
        很明显，使用层序遍历比较方便
        '''
        que=deque()
        if root:#根据题意，至少一个节点
            que.append(root)
        res=0
        while que:
            length=len(que)
            for i in range(length):
                if i==0:#最左边的就是每层第一个
                    res=que[0].val
                node=que.popleft()
                if node.left:
                    que.append(node.left)
                if node.right:
                    que.append(node.right)
        return res

# @lc code=end

