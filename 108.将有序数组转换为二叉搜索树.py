#
# @lc app=leetcode.cn id=108 lang=python3
#
# [108] 将有序数组转换为二叉搜索树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        def makeTree(leftidx,rightidx):
            if leftidx>rightidx:
                return None
            mid=(rightidx+leftidx)//2
            thisNode=TreeNode(nums[mid])
            thisNode.left=makeTree(leftidx,mid-1)
            thisNode.right=makeTree(mid+1,rightidx)
            return thisNode

        return  makeTree(0,len(nums)-1)
# @lc code=end

'''
详解看下面连接，实际上给定的是搜索树的中序遍历(递增)
https://leetcode-cn.com/problems/convert-sorted-array-to-binary-search-tree/solution/yi-wen-du-dong-shi-yao-shi-er-cha-sou-suo-shu-bst-/
'''
