#
# @lc app=leetcode.cn id=134 lang=python3
#
# [134] 加油站
#

# @lc code=start
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        start=0
        curSum=0
        totalSum=0
        for i in range(len(gas)):
            curSum+=gas[i]-cost[i]
            totalSum+=gas[i]-cost[i]
            if curSum<0:
                # 如果前i个和为负，则从第i+1个重新开始
                start=1+i
                curSum=0
        # 如果最后的和为负那么一定无法绕行，否则，则一定存在一个点(题目中说存在一个唯一的)
        if totalSum<0:
            return -1
        return start
# @lc code=end
'''
贪心算法
首先如果总油量减去总消耗大于等于零那么一定可以跑完一圈，说明 各个站点的加油站 剩油量rest[i]相加一定是大于等于零的。

每个加油站的剩余量rest[i]为gas[i] - cost[i]。

i从0开始累加rest[i]，和记为curSum，一旦curSum小于零，说明[0, i]区间都不能作为起始位置，起始位置从i+1算起，再从0计算curSum。
'''
