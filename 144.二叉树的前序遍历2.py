
# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 前序遍历-迭代-LC144_二叉树的前序遍历,迭代方法
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        # 根结点为空则返回空列表
        if root==None:
            return []
        result=[]
        stack=[root]
        while stack:
            node=stack.pop()
            result.append(node.val)#前序
            if node.right:#先将右孩子进栈在左孩子，这样出栈才能反过来
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
   
        return result