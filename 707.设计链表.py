#
# @lc app=leetcode.cn id=707 lang=python3
#
# [707] 设计链表
#

# @lc code=start
class Node:
    
    def __init__(self, val):
        self.val = val
        self.next = None

class MyLinkedList:
    '''
    需要注意两点：
    1，首先，本题的节点号是不包括虚拟头节点的
    2，其次，题目里说的第index个实际上是从0开始的，所以还是说的下标
    题目没说清楚
    '''
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self._head = Node(0)  # 虚拟头部节点
        self._count = 0  # 添加的节点数
        


    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        if index >= self._count or index < 0:
            return -1
        
        counter = 0
        tmp = self._head

        while counter < index:# 所以的这个模块，最后的cur都指向下表为index-1的节点(不包括头节点)
            counter += 1
            tmp = tmp.next
        
        return tmp.next.val



    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        self.addAtIndex(0,val)


    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        self.addAtIndex(self._count,val)

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        if self._count < index:
            return
        
        counter = 0
        cur = self._head
        while counter < index:
            counter += 1
            cur = cur.next

        tmp = cur.next
        node = Node(val)
        cur.next = node
        node.next = tmp
        self._count += 1


    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        if index >= self._count or index < 0:
            return 
        
        counter = 0
        cur = self._head
        while counter < index:
            counter += 1
            cur = cur.next
        
        next = cur.next.next
        cur.next = next
        self._count -= 1



# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
# @lc code=end

