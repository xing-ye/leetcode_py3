
# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 递归
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root==None:
            return []
        result=[]
        stack=[root]
        while stack:
            node=stack.pop()
            result.append(node.val)
            if node.left:#左先入栈，那么就后出栈
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
            #这样resul的实际上是按中右左，只要将数组逆转即可
        return result[::-1]