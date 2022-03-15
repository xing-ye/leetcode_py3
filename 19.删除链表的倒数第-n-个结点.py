#
# @lc app=leetcode.cn id=19 lang=python3
#
# [19] 删除链表的倒数第 N 个结点
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        head_dummy=ListNode(next=head)
        slow, fast = head_dummy, head_dummy

        while n!=0:#fast先往前走n步,最后指向第n个节点
            fast=fast.next
            n-=1
        while fast.next!=None:
            slow=slow.next
            fast=fast.next
        #fast 走到结尾后，slow的下一个节点为倒数第N个节点,
        slow.next=slow.next.next
        return head_dummy.next
        

# @lc code=end
'''
双指针的经典应用，如果要删除倒数第n个节点，
让fast移动n步，然后让fast和slow同时移动，
直到fast指向链表末尾。删掉slow所指向的节点就可以了。
可以画一些图，就很清晰了
'''
