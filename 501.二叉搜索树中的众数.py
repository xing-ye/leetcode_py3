#
# @lc app=leetcode.cn id=501 lang=python3
#
# [501] 二叉搜索树中的众数
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: TreeNode) -> List[int]:
        stack=[]
        res=[]
        cur=root
        pre=None
        count,maxcount=0,0

        while cur or stack:#如果刚开始就为空则不会执行
            if cur:
                stack.append(cur)
                cur=cur.left
            else:
                cur=stack.pop()#弹出的第一个恰好是最后一个左下角，栈
                if pre==None:
                    count=1
                elif pre.val==cur.val:
                    count+=1
                else:
                    count=1
                if count==maxcount:
                    res.append(cur.val)
                elif count>maxcount:
                    res.clear()
                    res.append(cur.val)
                    maxcount=count
                pre=cur
                cur=cur.right
        return res


# @lc code=end
'''
利用搜索树的中序遍历是一个有序的结果，可以直接进行判断前后是否相等
'''
