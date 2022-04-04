#
# @lc app=leetcode.cn id=222 lang=python3
#
# [222] 完全二叉树的节点个数
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    '''
    对于完全二叉树要注意有一个2^树深度  -1的式子，可以参考下面：
    https://programmercarl.com/0222.%E5%AE%8C%E5%85%A8%E4%BA%8C%E5%8F%89%E6%A0%91%E7%9A%84%E8%8A%82%E7%82%B9%E4%B8%AA%E6%95%B0.html#python
    '''
    def countNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        left=root.left
        right=root.right 
        leftHeight,rightHeight=0,0
        while left: #求左子树深度
            left=left.left 
            leftHeight+=1
        while right:
            '''
            因为考虑到完全二叉树，只有可能是右边的为空，所以左右这样求高度是可以的

            '''
            right=right.right 
            rightHeight+=1
        if rightHeight==leftHeight:
            return (2<<leftHeight)-1
            #注意(2<<1) 相当于2^2，所以leftHeight初始为0
        return  self.countNodes(root.left) + self.countNodes(root.right) + 1
        #加上中间的头节点
# @lc code=end

'''
对于普通的二叉树，其实很简单，有递归和迭代法：
class Solution:
    def countNodes(self, root: TreeNode) -> int:
        return self.getNodesNum(root)
        
    def getNodesNum(self, cur):
        if not cur:
            return 0
        leftNum = self.getNodesNum(cur.left) #左
        rightNum = self.getNodesNum(cur.right) #右
        treeNum = leftNum + rightNum + 1 #中
        return treeNum

import collections
class Solution:
    def countNodes(self, root: TreeNode) -> int:
        queue = collections.deque()
        if root:
            queue.append(root)
        result = 0
        while queue:
            size = len(queue)
            for i in range(size):
                node = queue.popleft()
                result += 1 #记录节点数量
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return result
'''