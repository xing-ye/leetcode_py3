#
# @lc app=leetcode.cn id=332 lang=python3
#
# [332] 重新安排行程
#
import collections
# @lc code=start
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # defaultdic(list) 是为了方便直接append
        tickets_dict = collections.defaultdict(list)
        for item in tickets:
            tickets_dict[item[0]].append(item[1])
        '''
        tickets_dict里面的内容是这样的
         {'JFK': ['SFO', 'ATL'], 'SFO': ['ATL'], 'ATL': ['JFK', 'SFO']})
        '''
        path = ["JFK"]
        def backtracking(start_point):
            # 终止条件
            if len(path) == len(tickets) + 1:
                # 这是因为把对拆成了链，所以会有多一个，可以参考测试用例
                return True
            tickets_dict[start_point].sort()#对目标地进行排序以方便删除重复场景
            for _ in tickets_dict[start_point]:
                #必须及时删除，避免出现死循环
                end_point = tickets_dict[start_point].pop(0)
                path.append(end_point)
                # 只要找到一个就可以返回了
                if backtracking(end_point):
                    return True
                path.pop()
                tickets_dict[start_point].append(end_point)
                #回溯，重新加入，所以每次for循环前都要排序

        backtracking("JFK")
        return path
# @lc code=end

'''
相比于回溯，也要注意defaltdic的用法
https://zhuanlan.zhihu.com/p/345741967
'''