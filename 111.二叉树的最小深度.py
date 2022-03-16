#
# @lc app=leetcode.cn id=111 lang=python3
#
# [111] 二叉树的最小深度
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # 层序遍历
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        dq,depth=deque([root]),1
        while dq:
            for i in range(len(dq)):
                tmp=dq.popleft()
                if not tmp.left and not tmp.right:
                    return depth
                if tmp.left:
                    dq.append(tmp.left)
                if tmp.right:
                    dq.append(tmp.right)
            depth+=1    

        return depth
# @lc code=end
'''
https://leetcode-cn.com/problems/minimum-depth-of-binary-tree/solution/111er-cha-shu-de-zui-xiao-shen-du-yan-du-mbrr/
deque是一种可以在两边加入和弹出的数据结构：

https://docs.python.org/zh-cn/3/library/collections.html?highlight=deque
'''
