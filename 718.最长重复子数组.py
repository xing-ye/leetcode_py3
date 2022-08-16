#
# @lc app=leetcode.cn id=718 lang=python3
#
# [718] 最长重复子数组
#

# @lc code=start
class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        len1,len2=len(nums1),len(nums2)
        if len1==0 or len2==0:
            return 0
        dp=[[0]*(len2+1) for _ in range(len1+1)]
        # len1+1行，len2+1列
        res=0
        # 因为dp计算的是前i-1个的，所以需要初始化比较长
        '''
        一定要注意数组的大小指什么，i指的是行，j是列
        '''
        for i in range(1,len1+1):
            for j in range(1,len2+1):
                if nums1[i-1]==nums2[j-1]:
                    dp[i][j]=dp[i-1][j-1]+1
                res=max(res,dp[i][j])

        return res
# @lc code=end
'''
是连续子序列。这种问题动规最拿手
dp[i][j] ：以下标i - 1为结尾的A，和以下标j - 1为结尾的B，最长重复子数组长度为dp[i][j]
我们在遍历dp[i][j]的时候i 和 j都要从1开始
'''
'''

'''