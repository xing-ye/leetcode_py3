'''
其实很多数组填充类的问题，都可以先预先给数组扩容带填充后的大小，然后在从后向前进行操作。

这么做有两个好处：

不用申请新数组。
从后向前填充元素，避免了从前先后填充元素要来的 每次添加元素都要将添加元素之后的所有元素向后移动。
'''

class Solution:
    def replaceSpace(self, s: str) -> str:
        counter=s.count(' ')
        res=list(s)
        res.extend([' ']*counter*2)
         # 每碰到一个空格就多拓展两个格子，1 + 2 = 3个位置存’%20‘
        left,right=len(s)-1,len(res)-1

        while left>=0:
            if res[left]!= ' ':
                res[right]=res[left]
                right-=1
            else:
                res[right-2: right+1]='%20'
                #左闭右开，这里是三个位置
                right-=3
            left-=1
        return ''.join(res)
