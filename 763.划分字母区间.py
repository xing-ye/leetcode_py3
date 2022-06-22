#
# @lc app=leetcode.cn id=763 lang=python3
#
# [763] 划分字母区间
#

# @lc code=start
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        hash=[0]*26
        for i in range(len(s)):
            hash[ord(s[i])-ord('a')]=i
            # 统计出每一个字幕出现的最远的值
            res=[]
            left,right=0,0
            for i in range(len(s)):
                right=max(right,hash[ord(s[i])-ord('a')])
                # 明确区域内每一个字母可能的最右边界
                if i==right:
                    # 如果正好到这个地方，那么前i个一定是只出现在一个段的最小段
                    res.append(right-left+1)
                    left=i+1
        return res

# @lc code=end

'''
这里的每个字母只出现在一个片段不是指只出现在该片段一次
统计每一个字符最后出现的位置
从头遍历字符，并更新字符的最远出现下标，
如果找到字符最远出现位置下标和当前下标相等了，则找到了分割点
'''