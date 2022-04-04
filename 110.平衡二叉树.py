#
# @lc app=leetcode.cn id=110 lang=python3
#
# [110] 平衡二叉树
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
    迭代比较难，能理解就好。
    '''
    def isBalanced(self, root: TreeNode) -> bool:
        return self.check_balance(root)!=-1
    def check_balance(self,root):
        if not root:
            return 0#对于叶子节点返回高度一
        leftHeigh=self.check_balance(root.left)
        if leftHeigh==-1:
            return -1#不需要判断全部，有一个不平衡即可
        rightHeigh=self.check_balance(root.right)
        if rightHeigh==-1:
            return -1#不需要判断全部，有一个不平衡即可
        return max(leftHeigh,rightHeigh)+1 if abs(leftHeigh-rightHeigh)<2 else -1
        #最后判断一次返回的结果是不是平衡(会不断从叶节点往上判断)

   
# @lc code=end
'''
如果不懂可以画图来看。要判断是否是平衡的，需要从小的二叉树一直判断到大的二叉树，所以使用后序比较好。
简单来说，因为求深度可以从上到下去查 所以需要前序遍历（中左右），而高度只能从下到上去查，所以只能后序遍历（左右中）
本题代码的逻辑其实是求的根节点的高度，而根节点的高度就是这棵树的最大深度，所以才可以使用后序遍历。
https://leetcode-cn.com/problems/balanced-binary-tree/solution/balanced-binary-tree-di-gui-fang-fa-by-jin40789108/
'''
