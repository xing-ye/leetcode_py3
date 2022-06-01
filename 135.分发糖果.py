#
# @lc app=leetcode.cn id=135 lang=python3
#
# [135] 分发糖果
#

# @lc code=start


class Solution:
    def candy(self, ratings: List[int]) -> int:
        res=[1] * len(ratings)
        for i in range(1,len(ratings)):
            if ratings[i]>ratings[i-1]:
                res[i]=res[i-1]+1
        for j in range(len(ratings)-2,-1,-1):#左闭右开
            if ratings[j]>ratings[j+1]:
                res[j]=max(res[j+1]+1,res[j])

        return sum(res)
# @lc code=end

'''
那么本题我采用了两次贪心的策略：

一次是从左到右遍历，只比较右边孩子评分比左边大的情况。
一次是从右到左遍历，只比较左边孩子评分比右边大的情况。
'''