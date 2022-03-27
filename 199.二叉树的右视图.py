#
# @lc app=leetcode.cn id=199 lang=python3
#
# [199] 二叉树的右视图
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        res=[]
        que=deque([root])
        #对于一个treenode并不是可迭代的，需要存入[]中才行
        while que:
            size=len(que)
            cur=que[-1]#每次获取每一行的最后一个节点即可
            res.append(cur.val)
            for _ in range(size):
                node=que.popleft()
                if node.left:
                    que.append(node.left)
                if node.right:
                    que.append(node.right)
        return res
# @lc code=end

