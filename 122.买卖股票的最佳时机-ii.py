#
# @lc app=leetcode.cn id=122 lang=python3
#
# [122] 买卖股票的最佳时机 II
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res=0
        for i in range(1,len(prices)):
            dayV=prices[i]-prices[i-1]
            res+=max(dayV,0)
        return res
# @lc code=end

'''
贪心算法,实际上将问题分解为计算每天的利润,只要求的正利润之和即可
'''