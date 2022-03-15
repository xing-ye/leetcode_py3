#
# @lc app=leetcode.cn id=383 lang=python3
#
# [383] 赎金信
#

# @lc code=start
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(magazine)<len(ransomNote):
            return False
        record=[0]*26
        for i in range(len(magazine)):
            record[ord(magazine[i])-ord('a')]+=1
        print(record)

        for i  in range(len(ransomNote)):
            record[ord(ransomNote[i])-ord('a')]-=1
        print(record)
        for i in range(len(record)):
            if record[i]<0:
                return False
                
        return True        
# @lc code=end
'''
创立一个长度为26得数组每个位置代表一个字母，只要统计两个
字符串中各个字母出现得次数即可
'''
