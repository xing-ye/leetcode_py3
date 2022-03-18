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
    # 递归法,可以画图理解
    def reverseList(self, head: ListNode) -> ListNode:

        def reverse(pre,cur):
            if not cur:#如果cur为空，退出条件
                return pre

            tmp=cur.next
            cur.next=pre

            return reverse(cur,tmp)

        return reverse(None,head)
   

# @lc code=end

