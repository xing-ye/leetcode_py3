#
# @lc app=leetcode.cn id=77 lang=python3
#
# [77] 组合
#

# @lc code=start
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res=[]#存储最终的结果
        path=[]#存储搜索的路径
        def backtrace(startIdx,n,k):
            if len(path)==k:
                res.append(path[:])
                return 
            for i in range(startIdx,n-(k-len(path))+2):#剪枝的操作
                path.append(i)
                backtrace(i+1,n,k)
                path.pop()  
        backtrace(1,n,k)             
        return res
# @lc code=end

'''
采用回溯的方法，回溯实际上是递归的一个附加产物，是一种搜索的方法，也可以叫做回溯搜索
回溯可以想像成一颗树的横向和纵向的过程，详细看代码随想录
要理解剪枝的改变，其中k-len(path)实际上时计算还有再选几个数，
而用n去减这个数，是说如果想要选满k个数，最晚要从哪个地方开始，
后面的+2是分两步的，第一个+1是因为这是左闭右开的，所以只有+1才能选到n-(k-len(path))+1
而这个值里的+1正是为了恰好选中第一个满足条件的结果，也是因为是左闭右开的，所以可以选到
https://programmercarl.com/0077.%E7%BB%84%E5%90%88.html#python

https://programmercarl.com/0077.%E7%BB%84%E5%90%88%E4%BC%98%E5%8C%96.html#%E5%85%B6%E4%BB%96%E8%AF%AD%E8%A8%80%E7%89%88%E6%9C%AC

'''