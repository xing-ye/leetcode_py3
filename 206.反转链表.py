#
# @lc app=leetcode.cn id=206 lang=python3
#
# [206] 反转链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next




class Solution:
    # 迭代法
    def reverseList(self, head: ListNode) -> ListNode:

        cur=head
        pre=None
        while cur!=None:
            tmp=cur.next
            cur.next=pre
            pre=cur
            cur=tmp
        return pre

   

# @lc code=end

