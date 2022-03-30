#
# @lc app=leetcode.cn id=101 lang=python3
#
# [101] 对称二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return False
        
        return self.compare(root.left,root.right)

    def compare(self,leftnode,rightnode):
        if not leftnode and not rightnode:
            return True   
        elif not leftnode and rightnode:
            return False
        elif not rightnode and leftnode:
            return False
        elif leftnode.val!=rightnode.val:
            return False
        
        flag1=self.compare(leftnode.left,rightnode.right)
        flag2=self.compare(leftnode.right,rightnode.left)

        return flag1 and flag2


# @lc code=end

'''
https://leetcode-cn.com/problems/symmetric-tree/solution/pythonpython3di-fa-dfs-by-null-o38-yy5y/
深度优先，需要注意的是轴对称，随意左边的左相当于右边的右
'''
'''
迭代的方法，使用队列
import collections
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        queue = collections.deque()
        queue.append(root.left) #将左子树头结点加入队列
        queue.append(root.right) #将右子树头结点加入队列
        while queue: #接下来就要判断这这两个树是否相互翻转
            leftNode = queue.popleft()
            rightNode = queue.popleft()
            if not leftNode and not rightNode: #左节点为空、右节点为空，此时说明是对称的
                continue
            
            #左右一个节点不为空，或者都不为空但数值不相同，返回false
            if not leftNode or not rightNode or leftNode.val != rightNode.val:
                return False
            queue.append(leftNode.left) #加入左节点左孩子
            queue.append(rightNode.right) #加入右节点右孩子
            queue.append(leftNode.right) #加入左节点右孩子
            queue.append(rightNode.left) #加入右节点左孩子
        return True
'''