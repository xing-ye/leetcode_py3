#
# @lc app=leetcode.cn id=429 lang=python3
#
# [429] N 叉树的层序遍历
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

from collections import deque


class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return []
        res=[]
        que=deque([root])
        #对于一个treenode并不是可迭代的，需要存入[]中才行
        while que:
            size=len(que)
            tmp=[]
            for _ in range(size):
                node=que.popleft()

                tmp.append(node.val)
                if node.children:
                    que.extend(node.children)
            res.append(tmp)
        return res
        
# @lc code=end

