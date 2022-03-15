#
# @lc app=leetcode.cn id=67 lang=python3
#
# [67] 二进制求和
#

# @lc code=start
class Solution:
    def addBinary(self, a: str, b: str) ->str:
        return bin(int(a,2)+int(b,2))[2:]
# @lc code=end

#参考自：https://leetcode-cn.com/problems/add-binary/solution/67-er-jin-zhi-qiu-he-pythonjie-fa-chun-c-ppif/