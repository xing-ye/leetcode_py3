#
# @lc app=leetcode.cn id=239 lang=python3
#
# [239] 滑动窗口最大值
#

# @lc code=start

from collections import deque
import re
class MyQueue:#单调队列(递减)
    def __init__(self) -> None:
        self.queue=deque()#deque是个双端队列
    def pop(self,value):
        if self.queue and value==self.queue[0]:
            self.queue.popleft()#list.pop()时间复杂度为O(n)因为需要前移,所以使用collections.deque(),只有O(1)
        
    def push(self,value):
        while self.queue and self.queue[-1]<value:
            self.queue.pop()
        self.queue.append(value)
    def maxnum(self):
        return self.queue[0]

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        result=[]
        tmp=MyQueue()
        for i in range(k):
            tmp.push(nums[i])
        
        result.append(tmp.maxnum())
        for i in range(k,len(nums)):
            tmp.pop(nums[i-k])
            tmp.push(nums[i])
            result.append(tmp.maxnum())

        return result
# @lc code=end

'''
答案参考自代码随想录：https://programmercarl.com/0239.%E6%BB%91%E5%8A%A8%E7%AA%97%E5%8F%A3%E6%9C%80%E5%A4%A7%E5%80%BC.html

其中的说明不是很清楚，下面再进行一下简单的说明:
1,实际上使用了双指针对nums控制，来控制比较的始终是K个
2，而保存这k个的数据结构是自己实现的一个单调队列
它的主要功能是，只保存一个单调递减的队列(小于等于k)
所以push时需要将比将要push的value小的删掉
而pop时，是需要判断nums的左指针是不是恰好到了保存的最大值的位置
3，最后，每一次的最大值都保存到result中，返回

deque的说明见此：https://blog.csdn.net/qq_28304687/article/details/79088491
'''