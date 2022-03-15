#
# @lc app=leetcode.cn id=367 lang=python3
#
# [367] 有效的完全平方数
#

# @lc code=start
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num==1 or num==0:
            return True
        low,high=1,num                                    
        while low<=high:
            mid=low+(high-low)//2
            if mid*mid==num:
                return True
            elif mid*mid<num:
                low=mid+1
            elif mid*mid>num:
                high=mid-1
        return False
# @lc code=end
'''
可以看成一个二分查找过程
'''
