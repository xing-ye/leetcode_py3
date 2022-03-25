#
# @lc app=leetcode.cn id=20 lang=python3
#
# [20] 有效的括号
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        for item in s:
            if item=='(':
                stack.append(')')
            elif item=='{':
                stack.append('}')
            elif item=='[':
                stack.append(']')
            elif item not in stack or stack[-1]!=item:
                return False
            else:
                stack.pop()
        return True if not stack else False
# @lc code=end
'''
用栈实现，只讲右括号入栈
'''
