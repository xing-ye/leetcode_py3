#
# @lc app=leetcode.cn id=93 lang=python3
#
# [93] 复原 IP 地址
#

# @lc code=start


class Solution:
    def is_valid(self, s: str, start: int, end: int) -> bool:
        '''
        可以看到是start和end的范围
        '''
        if start > end: return False
        # 若数字是0开头，不合法
        if s[start] == '0' and start != end:
            return False
        if not 0 <= int(s[start:end+1]) <= 255:
            return False
        return True
    def restoreIpAddresses(self, s: str) -> List[str]:
        res=[]
        if len(s)>12:
            return res

        def backtrace(s,startIdx,pointNum):
            if pointNum==3:#也就是已经划分过四个了
                if self.is_valid(s,startIdx,len(s)-1):
                    res.append(s[:])
                    return 
            # 单层递归逻辑
            for i in range(startIdx,len(s)):
                # [start_index, i]就是被截取的子串
                if self.is_valid(s,startIdx,i):
                    s=s[:i+1]+'.'+s[i+1:]
                    backtrace(s, i+2, pointNum+1)  # 在填入.后，下一子串起始后移2位
                    s = s[:i+1] + s[i+2:]    # 回溯
                else:
                # 若当前被截取的子串大于255或者大于三位数，直接结束本层循环
                    break
        backtrace(s,0,0)
        return res
            

# @lc code=end

