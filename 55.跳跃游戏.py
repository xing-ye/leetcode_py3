#
# @lc app=leetcode.cn id=55 lang=python3
#
# [55] 跳跃游戏
#

# @lc code=start



class Solution:
    def canJump(self, nums: List[int]) -> bool:
        cover=0 #表示已经覆盖的范围
        if len(nums)==1:
            return True
        i=0
        # 因为python无法在for循环中修改变量
        while i<=cover:
            cover=max(i+nums[i],cover)
            # 每次都去当前最大跳动数，对比获得最大的覆盖范围
            if cover >=len(nums)-1:return True
            # 当已经超过数组长度时一定可以跳到
            i+=1
        return False
        
# @lc code=end

'''
贪心算法的思路：
其实跳几步无所谓，关键在于可跳的覆盖范围！

不一定非要明确一次究竟跳几步，每次取最大的跳跃步数，这个就是可以跳跃的覆盖范围。

这个范围内，别管是怎么跳的，反正一定可以跳过来。
'''