#
# @lc app=leetcode.cn id=347 lang=python3
#
# [347] 前 K 个高频元素
#

# @lc code=start
import heapq
#时间复杂度：O(nlogk)
#空间复杂度：O(n)

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency={}
        for i in range(len(nums)):
            frequency[nums[i]]=frequency.get(nums[i],0)+1

        pri_que = [] #小顶堆
        for num,num_freq in frequency.items():
            heapq.heappush(pri_que,(num_freq,num)) 
            if len(pri_que)>k:
                heapq.heappop(pri_que)
        result=[0]*k
        #找出前K个高频元素，因为小顶堆先弹出的是最小的，所以倒序来输出到数组
        for i in range(k-1,-1,-1):
            result[i]=heapq.heappop(pri_que)[1]#只保存数字不保存频次
    
        
        return result
# @lc code=end

'''
参考自：https://programmercarl.com/0347.%E5%89%8DK%E4%B8%AA%E9%AB%98%E9%A2%91%E5%85%83%E7%B4%A0.html
首先使用集合进行统计它的频率，使用其值为key出现的次数为value
然后，将所有的统计结果存入一个小顶堆中（为了减少复杂度）即可找出最后的k个结果
其中使用了get()：https://www.runoob.com/python/att-dictionary-get.html
以及heapq():https://docs.python.org/zh-cn/3/library/heapq.html
'''