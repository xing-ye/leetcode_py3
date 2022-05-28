#
# @lc app=leetcode.cn id=45 lang=python3
#
# [45] 跳跃游戏 II
#

# @lc code=start
class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums)==1:return 0
        step=1# 统计步数，至少是一了
        curdistance=0
        nextdistance=0
        for i in range(len(nums)):
            nextdistance=max(i+nums[i],nextdistance)
            # 统计一下curdistance内下一步可以跳到的最大范围
            if i==curdistance:
                # 如果已经扫面完覆盖范围内的最大下一步
                if curdistance!=len(nums)-1:
                    # 当前还没有跳出
                    curdistance=nextdistance
                    # 跳到可以跳到的最大位置
                    if nextdistance>=len(nums)-1:
                        break
                        # 如果已经跳出了，则直接跳出循环
                    step+=1
                    # 没有跳出就在新的范围内计算即可   
        return step
# @lc code=end

'''
首先，题目说明总可以跳到最后的位置
同样使用贪心算法，思路如下：
同时统计当前能覆盖的范围，然后对当前覆盖的范围内进行统计，
计算出，下一步可以跳到的最大范围，如果到最后即跳出
如果下一步覆盖的还未跳出，那么步数加一
重新统计新的覆盖范围内新加入的位置计算下一步的最大范围，看是否可以跳出
'''