#
# @lc app=leetcode.cn id=538 lang=python3
#
# [538] 把二叉搜索树转换为累加树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.traversal(root,0)
        return root
    def traversal(self,root,pre):
        if not root:
            return None

        tmp=self.traversal(root.right,pre)#先计算右边的值
        if tmp:#如果右边不为空则相加上一步的值。
            root.val+=tmp
        else:#若为空则直接加0了（对于最右边的是最大的）
            root.val+=pre
        tmp2=self.traversal(root.left,root.val)#要注意传递的参数
        if tmp2:#计算到左边就是最后了，直接返回即可
            return tmp2
        return root.val#如果没有左节点，则计算到中间就是最后的了

        
# @lc code=end

'''
实际上按照反中序遍历递归即可：右中左
具体看：https://programmercarl.com/0538.%E6%8A%8A%E4%BA%8C%E5%8F%89%E6%90%9C%E7%B4%A2%E6%A0%91%E8%BD%AC%E6%8D%A2%E4%B8%BA%E7%B4%AF%E5%8A%A0%E6%A0%91.html#python
'''