#
# @lc app=leetcode.cn id=416 lang=python3
#
# [416] 分割等和子集
#

# @lc code=start
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        target=sum(nums)
        if target%2==1:# 取余
            return False
        # 如果和为奇数，那么一定不能平均分割
        dp=[0]*10001
        target //= 2
        '''
        题目说明，每个数最大为100，做多有两百个数，那么之和最大为两万
        背包只需要统计它的一半就可以了，也就是dp[10000]
        '''
        for i in range(len(nums)):# 物品数量
            for j in range(target,nums[i]-1,-1):# 背包容量
                # 左闭右开，所以是target到nums[i]， 每一个元素一定是不可重复放入，所以从大到小遍历
                dp[j]=max(dp[j],dp[j-nums[i]]+nums[i])
        return target==dp[target]
        # 如果dp[j] == j 说明，集合中的子集总和正好可以凑成总和j
# @lc code=end
'''
dp[j]表示 背包总容量是j，最大可以凑成j的子集总和为dp[j],即dp[j]是实际装的容量。
01背包的递推公式为：dp[j] = max(dp[j], dp[j - weight[i]] + value[i])

本题，相当于背包里放入数值，那么物品i的重量是nums[i]，其价值也是nums[i]。

所以递推公式：dp[j] = max(dp[j], dp[j - nums[i]] + nums[i])
'''