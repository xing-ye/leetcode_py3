#
# @lc app=leetcode.cn id=242 lang=python3
#
# [242] 有效的字母异位词
#

# @lc code=start
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        record=[0]*26
        for i in range(len(s)):
            record[ord(s[i])-ord('a')]+=1
        print(record)

        for i  in range(len(t)):
            record[ord(t[i])-ord('a')]-=1
        print(record)
        for i in range(len(record)):
            if record[i]!=0:
                return False
                
        return True
# @lc code=end
'''
创立一个长度为26得数组每个位置代表一个字母，只要统计两个
字符串中各个字母出现得次数即可
'''
