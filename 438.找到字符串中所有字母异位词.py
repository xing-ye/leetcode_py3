#
# @lc app=leetcode.cn id=438 lang=python3
#
# [438] 找到字符串中所有字母异位词
#

# @lc code=start
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        len_s,len_p=len(s),len(p)
        if len_s<len_p:
            return []
        count_s,count_p=[0]*26,[0]*26
        aNum=ord('a')
        ans=list()
        for i in range(len_p):
            count_p[ord(p[i])-aNum]+=1
            count_s[ord(s[i])-aNum]+=1
        if count_p==count_s:
            ans.append(0)
        for i in range(len_s-len_p):
            count_s[ord(s[i])-aNum]-=1
            count_s[ord(s[i+len_p])-aNum]+=1
            if count_s==count_p:
                ans.append(i+1)
        return ans


# @lc code=end
'''
这题我做过，就自己在做一次，加深体验
使用了移动窗口和hash
'''
