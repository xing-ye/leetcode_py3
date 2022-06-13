#
# @lc app=leetcode.cn id=56 lang=python3
#
# [56] 合并区间
#

# @lc code=start
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals)==0:return []
        intervals.sort(key=lambda x:x[0])
        # 将左边界从小到大排序
        res=[]
        res.append(intervals[0])
        for i in range(1,len(intervals)):
            tmp=res[-1]
            # 不断或许最后面的进行合并，刚开始时就是intervals[0]
            if tmp[1]>=intervals[i][0]:
                # 如果前面的右边界比后面的左边界大，就合并
                res[-1]=[tmp[0],max(tmp[1],intervals[i][1])]
                # 更新最后一个的范围
            else:
                res.append(intervals[i])
        return res
# @lc code=end

'''
贪心，先按一个边界排序，在对另一个进行判断
'''