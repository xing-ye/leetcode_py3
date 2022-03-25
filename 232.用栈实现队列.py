#
# @lc app=leetcode.cn id=232 lang=python3
#
# [232] 用栈实现队列
#

# @lc code=start
from curses.ascii import FS


class MyQueue:

    def __init__(self):
        self.stack_in=[]
        self.stack_out=[]



    def push(self, x: int) -> None:
        self.stack_in.append(x)


    def pop(self) -> int:
        '''
        由于队列先入先出，所以一定要先从输入栈
        换到输出栈，在输出
        '''
        if self.empty():
            return None
        if self.stack_out:
            return self.stack_out.pop()
        else:
            for i in range(len(self.stack_in)):
                self.stack_out.append(self.stack_in.pop())
            return self.stack_out.pop()


    def peek(self) -> int:
        '''
        返回队列开头的元素
        '''
        ans=self.pop()
        self.stack_out.append(ans)
        #由于在pop里删除了，而peek并不要求删除，所以重新加进去
        return ans


    def empty(self) -> bool:
        if not self.stack_in and not self.stack_out:
            return True
        else:
            return False



# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
# @lc code=end

'''
https://programmercarl.com/0232.%E7%94%A8%E6%A0%88%E5%AE%9E%E7%8E%B0%E9%98%9F%E5%88%97.html#%E6%80%9D%E8%B7%AF
'''