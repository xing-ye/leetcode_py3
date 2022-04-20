#
# @lc app=leetcode.cn id=98 lang=python3
#
# [98] 验证二叉搜索树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right



class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        cur_max=-float("INF")
        def _isValidBST(root):
            nonlocal cur_max #用来声明外部的局部变量
            
            if not root:# 判断到最后叶节点了，返回true
                return True
            is_left_valid=_isValidBST(root.left)
            if cur_max<root.val:
                cur_max=root.val
            else:
                return False
            is_right_valid=_isValidBST(root.right)
            return is_left_valid and is_right_valid
        
        return _isValidBST(root)



# @lc code=end

'''
递归的方法：
利用中序遍历是一个由小到大的升序遍历来写
'''