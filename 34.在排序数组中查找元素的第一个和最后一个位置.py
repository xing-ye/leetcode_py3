#
# @lc app=leetcode.cn id=34 lang=python3
#
# [34] 在排序数组中查找元素的第一个和最后一个位置
#

# @lc code=start
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def getRightBorder(nums:List[int], target:int) -> int:
            left, right = 0, len(nums)-1
            rightBoder = -2 # 记录一下rightBorder没有被赋值的情况
            while left <= right:
                middle = left + (right-left) // 2
                if nums[middle] > target:
                    right = middle - 1
                else: # 寻找右边界，nums[middle] == target的时候更新left
                    left = middle + 1
                    rightBoder = left
    
            return rightBoder
        
        def getLeftBorder(nums:List[int], target:int) -> int:
            left, right = 0, len(nums)-1 
            leftBoder = -2 # 记录一下leftBorder没有被赋值的情况
            while left <= right:
                middle = left + (right-left) // 2
                if nums[middle] >= target: #  寻找左边界，nums[middle] == target的时候更新right
                    right = middle - 1;
                    leftBoder = right;
                else:
                    left = middle + 1
            return leftBoder
        leftBoder = getLeftBorder(nums, target)
        rightBoder = getRightBorder(nums, target)
        # 情况一
        if leftBoder == -2 or rightBoder == -2: return [-1, -1]
        # 情况三
        if rightBoder -leftBoder >1: return [leftBoder + 1, rightBoder - 1]
        # 情况二
        return [-1, -1]
# @lc code=end

'''
基本上看到logn的时间复杂度就是二分查找
这里的代码还有待精简，基本上就是用了两次二分查找
可以画图演算一遍
'''