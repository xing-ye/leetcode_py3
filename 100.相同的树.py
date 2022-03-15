#
# @lc app=leetcode.cn id=100 lang=python3
#
# [100] 相同的树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
       #bfs广度优先，需要借助队列了
        if not p and not q:
            return True
        elif not p or  not q:
            return False
        queueP=[p]
        queueQ=[q]#先将两个头节点加入
        while queueP and queueQ:
            nodeP=queueP.pop(0)
            nodeQ=queueQ.pop(0)
            if nodeP.val!=nodeP.val:
                return False
            leftP,rightP=nodeP.left,nodeP.right
            leftQ,rightQ=nodeQ.left,nodeQ.right 
            if (not leftP) ^ (not leftQ):
                return False
            if (not rightP) ^ (not rightQ):
                return False
            if leftP:
                queueP.append(leftP)
            if leftQ:
                queueQ.append(leftQ)
            if rightP:
                queueP.append(rightP)
            if rightQ:
                queueQ.append(rightQ)
        #循环结束后，只有当两个队列都为空时才会返回true
        return not queueP and not queueQ

# @lc code=end
'''
利用深度搜索和广度搜索，只要路径相同的就是相同的树
https://leetcode-cn.com/problems/same-tree/solution/100-xiang-tong-de-shu-by-edelweisskoko-3iqr/
'''

