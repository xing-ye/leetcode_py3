#
# @lc app=leetcode.cn id=541 lang=python3
#
# [541] 反转字符串 II
#

# @lc code=start
class Solution:
    def reverseStr(self, s: str, k: int) -> str:

        def reverseString(text):

            left,right=0,len(text)-1
            while left<right:
                text[left],text[right]=text[right],text[left]
                left+=1
                right-=1 
            return text
        res = list(s)

        for cur in range(0, len(s), 2 * k):
            res[cur: cur + k] = reverseString(res[cur: cur + k])
        
        return ''.join(res)

        
# @lc code=end
"""
1. 使用range(start, end, step)来确定需要调换的初始位置
2. 对于字符串s = 'abc'，如果使用s[0:999] ===> 'abc'。
字符串末尾如果超过最大长度，则会返回至字符串最后一个位置，这个特性可以避免一些边界条件的处理。
3. 用切片整体替换，而不是一个个替换.
"""
