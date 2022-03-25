#
# @lc app=leetcode.cn id=150 lang=python3
#
# [150] 逆波兰表达式求值
#

# @lc code=start
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        for item in tokens:
            if item not in {'+','-','*','/'}:
                stack.append(item)
            else:
                second_num,first_num=stack.pop(),stack.pop()
                res=int(eval(f'{first_num}{item}{second_num}'))
                stack.append(res)

        return int(stack.pop())#若tokens只有一个数时，一开始存的时一个字符
# @lc code=end
'''
参考自：https://programmercarl.com/0150.%E9%80%86%E6%B3%A2%E5%85%B0%E8%A1%A8%E8%BE%BE%E5%BC%8F%E6%B1%82%E5%80%BC.html#_150-%E9%80%86%E6%B3%A2%E5%85%B0%E8%A1%A8%E8%BE%BE%E5%BC%8F%E6%B1%82%E5%80%BC
实际上就是后缀表达式的计算过程,这里使用栈计算
其中有几个需要注意的：
1，首先pop的实际上时后面的操作数，
2，f'{}'叫做f-string,其中括号中的内容会自动替换为值并合成一个大的字符串
详见：https://docs.python.org/zh-cn/3/tutorial/inputoutput.html
3，eval()是用来计算表达式的，如果不用这个就自行判断操作符即可，
详见：https://www.runoob.com/python/python-func-eval.html
'''
