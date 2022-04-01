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

# 迭代法
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        '''
        如果把这个当成两个队列去比较会非常的繁琐
        直接把其当作树的两个左右节点，就会好很多
        '''
        if not p and not q: return True
        if not p or not q: return False
        que = collections.deque()
        que.append(p)
        que.append(q)
        while que:
            leftNode = que.popleft()
            rightNode = que.popleft()
            if not leftNode and not rightNode: continue 
            if not leftNode or not rightNode or leftNode.val != rightNode.val: return False 
            que.append(leftNode.left)
            que.append(rightNode.left)
            que.append(leftNode.right)
            que.append(rightNode.right)
            #加入顺序实际上就是两两需要比较的的顺序
        return True


# @lc code=end

'''
class Solution:
  
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
       #bfs广度优先，需要借助队列了
        if not p and not q:
            return True
        elif not p or  not q:
            return False
        elif p.val!=q.val:
            return False
        else:
            return self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)

'''