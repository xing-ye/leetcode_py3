#
# @lc app=leetcode.cn id=88 lang=python3
#
# [88] 合并两个有序数组
#

# @lc code=start
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        now = m+n-1
        while m > 0 and n > 0:
            if nums1[m-1] >= nums2[n-1]:
                nums1[now] = nums1[m-1]
                m -= 1
            else:
                nums1[now] = nums2[n-1]
                n -= 1
            now -= 1
        if m == 0:
            for i in range(n):
                nums1[i] = nums2[i]

        
# @lc code=end
# 采用从后部排序的思想，即先将大的排好，如果最后先排序完的nums1那么再将nums2加入即可，因为二者都是已排好的非降序数组
'''
可以参考一下两个：
https://leetcode-cn.com/problems/merge-sorted-array/solution/python-yi-xing-dai-ma-fang-an-he-wan-zhe-vfet/
https://leetcode-cn.com/problems/merge-sorted-array/solution/hua-jie-suan-fa-88-he-bing-liang-ge-you-xu-shu-zu-/
'''
