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
要理解剪枝的改变，不明白的去画个图。
https://programmercarl.com/0077.%E7%BB%84%E5%90%88.html#python
'''