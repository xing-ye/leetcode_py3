#
# @lc app=leetcode.cn id=53 lang=python3
#
# [53] 最大子数组和
#

# @lc code=start
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        tmp=nums[0]
        max_=tmp
        for i  in range(1,len(nums)):
            if tmp+nums[i]>nums[i]:
                max_=max(max_,tmp+nums[i])
                tmp=tmp+nums[i]
            else:
                 max_=max(max_,nums[i],tmp,tmp+nums[i])
                 tmp=nums[i]
        return max_
# @lc code=end

'''
参考自：
https://leetcode-cn.com/problems/maximum-subarray/solution/bao-li-qiu-jie-by-pandawakaka/

最关键的核心思想就是是否加前面的部分，以当前的i为锚点，如果i之前的内容加了之后还变小了就不加。

'''
