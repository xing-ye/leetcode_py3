#
# @lc app=leetcode.cn id=454 lang=python3
#
# [454] 四数相加 II
#

# @lc code=start
class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        record=dict()
        for i in nums1:
            for j in nums2:
                if i+j in record:
                    record[i+j]+=1 #这里key是和，而value是同样和的个数
                else:
                    record[i+j]=1
        count=0
        for i in nums3:
            for j in nums4:
                key=-i-j#实际上就是0-前两个的和
                if key in record:
                    count+=record[key]
        
        return count

# @lc code=end

'''
这题可以采用与1相同的做法，因为这题只求次数。
具体的可以看这个连接：https://programmercarl.com/0454.%E5%9B%9B%E6%95%B0%E7%9B%B8%E5%8A%A0II.html#%E5%85%B6%E4%BB%96%E8%AF%AD%E8%A8%80%E7%89%88%E6%9C%AC
'''