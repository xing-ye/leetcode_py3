#
# @lc app=leetcode.cn id=406 lang=python3
#
# [406] 根据身高重建队列
#

# @lc code=start
class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people.sort(key=lambda x:(-x[0],x[1]))
        # 先按照升高由大到小排i，因为sort默认升序排序所以要负号
        # 然后再按照k由小到大排
        que=[]
        for p in people:
            que.insert(p[1],p)
            # 按照k进行插入。
        return que
# @lc code=end
'''
https://programmercarl.com/0406.%E6%A0%B9%E6%8D%AE%E8%BA%AB%E9%AB%98%E9%87%8D%E5%BB%BA%E9%98%9F%E5%88%97.html#%E6%80%9D%E8%B7%AF
先按照身高从大到小排序，其中k小的排在前面
这样排序后，直选哟再按照k所表示的位置，从前往后依次插入即可，因为后插入的
一定小于前面的所有值，所以不会对后面的相同k的造成影响
'''

