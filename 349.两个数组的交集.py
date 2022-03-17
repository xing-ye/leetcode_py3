#
# @lc app=leetcode.cn id=349 lang=python3
#
# [349] 两个数组的交集
#

# @lc code=start
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
         return list(set(nums1) & set(nums2))    # 两个数组先变成集合，求交集后还原为数组
# @lc code=end
'''
这题用python很简单，但是需要说明一下为什么用set：
因为相比于字母，数字的范围太广，所以用数组是不明智的
那么为什么不是所有的hash都用set呢，是因为直接使用set 不仅占用空间比数组大，而且速度要比数组慢，set把数值映射到key上都要做hash计算的。

不要小瞧 这个耗时，在数据量大的情况，差距是很明显的。
'''

