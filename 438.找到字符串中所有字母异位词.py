#
# @lc app=leetcode.cn id=438 lang=python3
#
# [438] 找到字符串中所有字母异位词
#

# @lc code=start
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        lens,lenp= len(s),len(p)
        if lens<lenp:
           return []
        ans=[]
        count_p=[0]*26#分别统计两个串的字符个数
        count_s=[0]*26
        for i in range(lenp):#分别计算前lenp的字符个数
           count_p[ord(p[i])-ord('a')]+=1
           count_s[ord(s[i])-ord('a')]+=1
        if count_p==count_s:
            ans.append(0)
        for i in range(lens-lenp):
            count_s[ord(s[i])-ord('a')]-=1
            count_s[ord(s[i+lenp])-ord('a')]+=1
            if count_p==count_s:
                ans.append(i+1)#因为i是控制删除的部分
        return ans

'''
这里同时使用了hash表和滑动窗口的方法，还有更进一步的简化方法
但是我没看懂，具体看：https://leetcode-cn.com/problems/find-all-anagrams-in-a-string/solution/zhao-dao-zi-fu-chuan-zhong-suo-you-zi-mu-xzin/
有需要可以画图试试

'''


# @lc code=end

