#
# @lc app=leetcode.cn id=69 lang=python3
#
# [69] x 的平方根 
#

# @lc code=start
class Solution:
    def mySqrt(self, x: int) -> int:
        if x==0 or x==1:
            return x
        low,high,res=1,x,-1
        while low<=high:
            mid=(low+high)//2
            if mid*mid<=x:
                res=mid
                low=mid+1
            else:
                high=mid-1

        return res
# @lc code=end
"""
参考自：
其实就相当于一个二分查找
https://leetcode-cn.com/problems/sqrtx/solution/acm-xuan-shou-tu-jie-leetcode-sqrtx-by-r-p8fx/
"""
