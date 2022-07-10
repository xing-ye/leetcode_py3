#
# @lc app=leetcode.cn id=1049 lang=python3
#
# [1049] 最后一块石头的重量 II
#

# @lc code=start
class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        allweight=sum(stones)
        target=allweight//2
        # 背包最多存一半就可以，尽量装到容量为target的背包所能背的最大重量。
        # 这里不直接设置dp为[0]*(target+1)是因为可能存在比target重的石头
        # dp=[0]*1501
        dp=[0]*(target+1)
        # 根据题意，最多3000，一半就是1500，所以背包最大可能的容量就是1500
        for i in range(len(stones)):
            # 对所有石头遍历
            for j in range(target,stones[i]-1,-1):
                # 对所有容量大于stones[i]的背包做判断
                dp[j]=max(dp[j],dp[j-stones[i]]+stones[i])
        return allweight-2*dp[target]
        # 最后dp[target]里是容量为target的背包所能背的最大重量。
# @lc code=end

'''
实际上就是尽量将石头分成两堆重量相近的，那么最后的重量就会最少，这也就转换成了01背包问题，即找到里是容量为target的背包所能背的最大重量dp[target]
dp[j] = max(dp[j], dp[j - stones[i]] + stones[i]);
dp[j]表示容量为j的背包，最多可以背dp[j]这么重的石头
所以用01背包是为例能够统计怎么分，才可以最大限度的装到最接近总量一半的石头
'''