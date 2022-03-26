
# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right



#递归方法
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root==None:
            return []
        result=[]
        stack=[]#对于中序不能将root存入
        cur=root
        while cur or stack:#只要有一个不空就继续
            if cur:
                stack.append(cur)
                cur=cur.left#找到最左边的
            else:
                node=stack.pop()
                result.append(node.val)
                cur=node.right
        return result