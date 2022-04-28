#
# @lc app=leetcode.cn id=17 lang=python3
#
# [17] 电话号码的字母组合
#

# @lc code=start
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res=[]
        if not digits:
            return []
        phone = {'2':['a','b','c'],
                 '3':['d','e','f'],
                 '4':['g','h','i'],
                 '5':['j','k','l'],
                 '6':['m','n','o'],
                 '7':['p','q','r','s'],
                 '8':['t','u','v'],
                 '9':['w','x','y','z']}
        def backtrack(conbination,nextdigit):
            if len(nextdigit)==0:
                res.append(conbination)
            else:
                for letter in phone[nextdigit[0]]:
                    #获取第一个数字中的字母
                    backtrack(conbination+letter,nextdigit[1:])
        
        backtrack("",digits)
        return res

# @lc code=end

'''
采用回溯的方法
当题目中出现 “所有组合” 等类似字眼时，我们第一感觉就要想到用回溯。
参考自：https://leetcode-cn.com/problems/letter-combinations-of-a-phone-number/solution/hui-su-dui-lie-tu-jie-by-ml-zimingmeng/
'''