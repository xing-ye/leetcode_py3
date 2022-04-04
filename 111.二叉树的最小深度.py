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
                #每一次for循环实际上都是在弹出一层，然后加入下一层的过程
                #所以，这里depth都是一样的，在处理完后加一即可
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
需要注意的是，只有当左右孩子都为空的时候，才说明遍历的最低点了。
如果其中一个孩子为空则不是最低点
'''
'''
与最大深度的区别(同样是层序遍历)：
最小深度，只要有节点的左右节点不存在就直接返回深度了
而最大深度，并不判读这个，二是将下一层的节点全部存入，直到最后一层。
'''
