#
# @lc app=leetcode.cn id=435 lang=python3
#
# [435] 无重叠区间
#

# @lc code=start
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if len(intervals)==0: return 0
        intervals.sort(key=lambda x:x[1])
        # 按照右边进行排序
        count=1 #记录非交叉区间的数，至少是有一个的
        end=intervals[0][1]
        # 从左边开始计算，先保存初始点
        for i in range(1,len(intervals)):
            if end<=intervals[i][0]:
                count+=1
                end=intervals[i][1]
            
        return len(intervals)-count
# @lc code=end
'''
与452射气球的原理相同，贪心算法
首先，需要对所有区间按照start或者end进行排序，这里按照end
排序后，我们只需要统计有多少区间的end在某一区间的start内，即可计算出要删除的数目
因为这里只需统计数目，所及不用管怎么删，删哪个
'''
