#
# @lc app=leetcode.cn id=202 lang=python3
#
# [202] 快乐数
#

# @lc code=start
class Solution:
    def isHappy(self, n: int) -> bool:
        def caculate(num):
            sum=0
            while num:
                sum+=(num%10)**2#求余
                num=num//10
            return sum
        record=set()
        while True:
            n=caculate(n)
            if n==1:
                return True
            if n in record:
                return False
            else: 
                record.add(n)
                
        
# @lc code=end

'''
这道题本身的想法很简单,只需要不停计算即可。
但是需要注意，可能存在无限循环的情况，条件就是，计算出的和sum在后面又出现
判断是否出现，就想到使用hash表的set
'''