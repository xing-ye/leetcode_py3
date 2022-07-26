#
# @lc app=leetcode.cn id=337 lang=python3
#
# [337] 打家劫舍 III
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: TreeNode) -> int:
        result = self.rob_tree(root)
        return max(result[0], result[1])
    
    def rob_tree(self, node):
        # 下标为0记录不偷该节点所得到的的最大金钱，下标为1记录偷该节点所得到的的最大金钱。
        if node is None:
            return (0, 0) # (偷当前节点金额，不偷当前节点金额)
            # 这里当遍历到叶节点时返回，所以left和right都先初始化为0
        left = self.rob_tree(node.left)
        right = self.rob_tree(node.right)
        # 后序遍历
        val1 = node.val + left[1] + right[1] # 偷当前节点，不能偷子节点
        val2 = max(left[0], left[1]) + max(right[0], right[1]) # 不偷当前节点，可偷可不偷子节点
        return (val1, val2)
    
# @lc code=end

'''
树形dp,因为是在树上进行状态转移
所以本题dp数组就是一个长度为2的数组！
首先明确的是使用后序遍历。即从下往上推，因为通过递归函数的返回值来做下一步计算。

所以dp数组（dp table）以及下标的含义：下标为0记录不偷该节点所得到的的最大金钱，下标为1记录偷该节点所得到的的最大金钱。

如果是偷当前节点，那么左右孩子就不能偷，
val1 = cur->val + left[0] + right[0]; 
（如果对下标含义不理解就在回顾一下dp数组的含义）

如果不偷当前节点，那么左右孩子就可以偷，至于到底偷不偷一定是选一个最大的，所以：
val2 = max(left[0], left[1]) + max(right[0], right[1]);
'''