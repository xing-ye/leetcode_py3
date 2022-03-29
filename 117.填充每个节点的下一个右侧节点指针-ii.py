#
# @lc app=leetcode.cn id=117 lang=python3
#
# [117] 填充每个节点的下一个右侧节点指针 II
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return None
        que=[root]
        #使用数组实际上增加了复杂度，可以使用deque([root]) leftpop
        #注意必须使用[root]，感觉就像是que=[root]在加上个结构声明一样
        while que:
            n=len(que)
            for i in range(n):
                node=que.pop(0)
                if node.left:
                    que.append(node.left)
                if node.right:
                    que.append(node.right)
                if i==n-1:
                    break #最后一个节点不指向下一个
                node.next=que[0]
        return root
        
        
# @lc code=end
'''
本题不再是完全的二叉树，但是在层序遍历中仍是相邻的，所以与116相同
'''
