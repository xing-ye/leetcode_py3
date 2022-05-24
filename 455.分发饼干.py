#
# @lc app=leetcode.cn id=455 lang=python3
#
# [455] 分发饼干
#

# @lc code=start
class Solution:
    def findContentChildren(self, g: List[int], s:List[int]) -> int:
        g.sort()
        s.sort()
        count=0
        for i in range(len(s)):
            if count<len(g) and s[i]>=g[count]:
                # 小的饼干优先满足小胃口的
                count+=1
        return count
# @lc code=end

