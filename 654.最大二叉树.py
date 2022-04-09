#
# @lc app=leetcode.cn id=654 lang=python3
#
# [654] 最大二叉树
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
    递归的方法
    '''
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        if not nums:
            return None
        maxVal=max(nums)
        maxIdx=nums.index(maxVal)
        root=TreeNode(maxVal)
        left=nums[:maxIdx]
        right=nums[maxIdx+1:]
        root.left=self.constructMaximumBinaryTree(left)
        root.right=self.constructMaximumBinaryTree(right)

        return root
# @lc code=end

