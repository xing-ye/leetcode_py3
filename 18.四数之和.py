#
# @lc app=leetcode.cn id=18 lang=python3
#
# [18] 四数之和
#


# 哈希表法
class Solution(object):
    def fourSum(self, nums, target)-> List[List[int]]:
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        # use a dict to store value:showtimes
        hashmap = dict()
        for n in nums:
            if n in hashmap:
                hashmap[n] += 1
            else: 
                hashmap[n] = 1
        
        # good thing about using python is you can use set to drop duplicates.
        ans = set()
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                for k in range(j + 1, len(nums)):
                    val = target - (nums[i] + nums[j] + nums[k])
                    if val in hashmap:
                        # make sure no duplicates.
                        '''
                    例如，2 2 2 -6，只有用2的数量大于3才可以保证，可以构成一个结果
                        '''
                        count = (nums[i] == val) + (nums[j] == val) + (nums[k] == val)
                        if hashmap[val] > count:
                            ans.add(tuple(sorted([nums[i], nums[j], nums[k], val])))
                    else:
                        continue
        return list(ans)

# @lc code=end

'''
虽然要求的是不能有重复的，yonghash会比较麻烦，但是对于python
可以使用set()来存储结果，一定不会有重复的。然后用hash来判断
https://programmercarl.com/0018.%E5%9B%9B%E6%95%B0%E4%B9%8B%E5%92%8C.html#%E5%85%B6%E4%BB%96%E8%AF%AD%E8%A8%80%E7%89%88%E6%9C%AC
'''