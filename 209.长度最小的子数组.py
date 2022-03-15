#
# @lc app=leetcode.cn id=209 lang=python3
#
# [209] 长度最小的子数组
#

# @lc code=start
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        res=float('inf')#定义一个无限大的数
        sum,idx=0,0
        for i in range(len(nums)):
            sum+=nums[i]
            while sum>= target:
                length=(i-idx)+1
                res=min(res,length)
                sum-=nums[idx]
                idx+=1
            
        return 0 if res==float('inf') else res
        #若没有赋值则返回0
# @lc code=end
'''
这里采用的方法叫做滑动窗口法： https://programmercarl.com/0209.%E9%95%BF%E5%BA%A6%E6%9C%80%E5%B0%8F%E7%9A%84%E5%AD%90%E6%95%B0%E7%BB%84.html#%E5%85%B6%E4%BB%96%E8%AF%AD%E8%A8%80%E7%89%88%E6%9C%AC
这里的时间复杂度实际上是O(n)，并不是有两个循环就是O(n^2)，主要是看每一个元素被操作的次数。
'''
