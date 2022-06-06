#
# @lc app=leetcode.cn id=452 lang=python3
#
# [452] 用最少数量的箭引爆气球
#

# @lc code=start

class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if len(points)==0:return 0
        points.sort(key=lambda x:x[0])
        # 按照左边界由小到大排序
        result=1
        for i in range(1,len(points)):
            if points[i][0]>points[i-1][1]:
                # 气球i和气球i-1不挨着，注意这里不是>=
                result+=1
            else:
                points[i][1] = min(points[i - 1][1], points[i][1]) 
                # 更新重叠气球最小右边界
                # 如果气球重叠了，重叠气球中右边边界的最小值 之前的区间一定需要一个弓箭。
        return result
# @lc code=end
'''
其思路是，将左边坐标按照从小到大排序
只要两个有重叠，那么记录其最小的右边坐标，这个位置一定要有一个剑
否则再往右第一个就射不到了
'''
