#
# @lc app=leetcode.cn id=203 lang=python3
#
# [203] 移除链表元素
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        dummy_head=ListNode(next=head)# 虚拟头节点，便于操作
        cur=dummy_head
        while cur.next!=None:
            if cur.next.val==val:
                cur.next=cur.next.next
                #python自带内存回收机制，所以不需要手动释放节点空间
            else:
                cur=cur.next
        return dummy_head.next
# @lc code=end

