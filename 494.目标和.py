#
# @lc app=leetcode.cn id=494 lang=python3
#
# [494] 目标和
#

# @lc code=start
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        sumall=sum(nums)

        if abs(target)>sumall or (sumall+target)%2 ==1: return 0
        bagsize=(sumall+target)//2
        dp=[0]*(bagsize+1)
        dp[0]=1# 初始化
        for i in range(len(nums)):
            for j in range(bagsize,nums[i]-1,-1):
                dp[j]+=dp[j-nums[i]]
        return dp[bagsize]
        # 
# @lc code=end
'''
假设加法的总和为x，那么减法对应的总和就是sum - x。

所以我们要求的是 x - (sum - x) = target,即2x-sum=target
，所以需要注意的是，target和sum应该是同奇同偶，
最后可以得到X的表达式，即x = (target + sum) / 2 ，所以X一定是偶数
这样就转换成01背包填容量为x的种类，
即dp[j] 表示：填满j（包括j）这么大容积的包，有dp[j]种方法
dp[j]+=dp[j-nums[i]]
之前都是求容量为j的背包，最多能装多少。本题则是装满有几种方法。其实这就是一个组合问题了，所以递推公式是不同的，有点像爬台阶
'''
