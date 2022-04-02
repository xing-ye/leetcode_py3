#
# @lc app=leetcode.cn id=559 lang=python3
#
# [559] N 叉树的最大深度
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""


class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root:
            return 0
        que=[root]
        deep=0
        while que:
            deep+=1
            tmp=[]
            for node in que:
                if node.children:
                    for node in node.children:
                        tmp.append(node)
            que=tmp
        return deep

        
# @lc code=end
''''
class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if root is None:
            return 0
        depth = 1
        for node in root.children:
            depth = max(depth, self.maxDepth(node) + 1)
        return depth



'''
