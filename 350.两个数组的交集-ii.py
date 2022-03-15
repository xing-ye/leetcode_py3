#
# @lc app=leetcode.cn id=350 lang=python3
#
# [350] 两个数组的交集 II
#

# @lc code=start
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        overlap=set(nums1)&set(nums2)
        ans=[]
        for i in overlap:
            ans+=[i]*min(nums1.count(i),nums2.count(i))

        return ans

# @lc code=end
'''
同样判断是否存在选择使用hash的set，与这题的1相同，
不过需要统计出次数，所以还需要进一步操作
'''
