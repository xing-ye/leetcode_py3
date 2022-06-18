#
# @lc app=leetcode.cn id=738 lang=python3
#
# [738] 单调递增的数字
#

# @lc code=start
class Solution:
    def monotoneIncreasingDigits(self, n: int) -> int:
        a=list(str(n))
        # 这样可以方便的获取不同的字母，而不需要一个一个的取
        for i in range(len(a)-1,0,-1):#左闭右开，不需要到0
            if int(a[i])<int(a[i-1]):
                # 需要递增，否则最好的是将a[i-1]-1，然后后面的都设为9
                # 这样做是因为我们要找，小于n的最大数
                a[i-1]=str(int(a[i-1])-1)
                a[i:]='9'*(len(a)-i)

        return int(''.join(a))

# @lc code=end

