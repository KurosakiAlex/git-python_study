'''
力扣第一题
两数之和
给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出 和为目标值 target  的那 两个 整数，并返回它们的数组下标。
'''


class Solution:
    def twoSum(self, nums, target):
        n = len(nums)
        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] + nums[j] == target:
                    return [i, j]

        return []

sol = Solution()

num01 = [2,5,9,3]

print(sol.twoSum(num01, 8))








nums = [2, 3, 5, 9]
target:7

class Solution:
    def twonum(self, nums, target):
        n = len(nums)
        for i in range(n):
            for j in range(i+1):

