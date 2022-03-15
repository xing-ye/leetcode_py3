#
# @lc app=leetcode.cn id=160 lang=python3
#
# [160] 相交链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        ta, tb = headA, headB
        while ta != tb:
            ta = ta.next if ta else headB
            tb = tb.next if tb else headA
        return tb

        
# @lc code=end

'''
作者：ceamanz
链接：https://leetcode-cn.com/problems/intersection-of-two-linked-lists-lcci/solution/shuang-zhi-zhen-zou-liang-bian-zou-dao-di-er-bian-/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

还有一种方法，先计算出两个得长度，然后减去差使二者从后尾对其，然后即可进行比较，详见：
https://programmercarl.com/%E9%9D%A2%E8%AF%95%E9%A2%9802.07.%E9%93%BE%E8%A1%A8%E7%9B%B8%E4%BA%A4.html#%E6%80%9D%E8%B7%AF
'''