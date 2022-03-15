#
# @lc app=leetcode.cn id=24 lang=python3
#
# [24] 两两交换链表中的节点
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # 明白指针的操作顺序很重要，需要好好看一下。
    def swapPairs(self, head: ListNode) -> ListNode:
        res=ListNode(next=head)# 虚拟头节点
        pre=res

        # 必须有pre的下一个和下下个才能交换，否则说明已经交换结束了
        while pre.next and pre.next.next:
            cur=pre.next
            pos=pre.next.next

            # pre，cur，post对应最左，中间的，最右边的节点
            #第一次时分别为头节点、还要交换的两个节点cur和pos
            cur.next=pos.next
            pos.next=cur
            pre.next=pos

            pre=pre.next.next
        return res.next


# @lc code=end

