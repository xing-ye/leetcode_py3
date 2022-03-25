#
# @lc app=leetcode.cn id=151 lang=python3
#
# [151] 颠倒字符串中的单词
#

# @lc code=start
class Solution:
    def reverseWords(self, s: str) -> str:
        #移除多余空格
        def trimSpace(tmp):
            left,right=0,len(tmp)-1
            while left<=right and tmp[left]==' ':
                left+=1
            while left<=right and tmp[right]==' ':
                right-=1
            res=[]
            while left<=right:
                if tmp[left]!=' ':
                    res.append(tmp[left])
                elif res[-1]!=' ':
                    res.append(tmp[left])
                left+=1
            return res
        
        # 反转字符
        def reverseString(res,left,right):
            while left<right:
                res[left],res[right]=res[right],res[left]
                left+=1
                right-=1
            return res
        # 翻转每个单词
        def reverseWord(res):
            start,end=0,0
            n=len(res)
            while start<n:
                while end<n and res[end]!=' ':
                    end+=1
                reverseString(res,start,end-1)
                start=end+1
                end+=1
            return res
        res=trimSpace(s)
        res=reverseString(res,0,len(res)-1)
        res=reverseWord(res)
               
        return ''.join(res)

# @lc code=end
'''
想一下，我们将整个字符串都反转过来，那么单词的顺序指定是倒序了，
只不过单词本身也倒序了，那么再把单词反转一下，单词不就正过来了。

所以解题思路如下：

移除多余空格
将整个字符串反转
将每个单词反转

其中的很多操作还可以改进，比如不使用辅助空间等
'''
