#
# @lc app=leetcode.cn id=15 lang=python3
#
# [15] 三数之和
#

# @lc code=start
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans=[]
        n=len(nums)
        nums.sort()
        for i in range(n):
            left=i+1
            right=n-1
            if nums[i]>0:
                break
            if i>=1 and nums[i]==nums[i-1]:
                continue
            while left<right:
                total=nums[i]+nums[left]+nums[right]
                if total>0:
                    right-=1
                elif total<0:
                    left+=1
                else:
                    ans.append([nums[i],nums[right],nums[left]])
                    while left != right and nums[left] == nums[left + 1]: left += 1
                    while left != right and nums[right] == nums[right - 1]: right -= 1
                    left += 1
                    right -= 1
        return ans          


# @lc code=end

'''
这里使用双指针法，而不是用hash，因为这里要求不能有重复的三元组。用hash会很麻烦
两数之和 就不能使用双指针法，因为1.
两数之和 (opens new window)要求返回的是索引下标， 
而双指针法一定要排序，一旦排序之后原数组的索引就被改变了。

如果1.两数之和 (opens new window)要求返回的是数值的话，
就可以使用双指针法了
'''