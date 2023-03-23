# Question 16:
    # 3Sum Closest
    # Given an integer array nums of length n and an integer target, find three integers in nums such that the sum is closest to target.
    # Return the sum of the three integers.

# The leetcode solution
class Solution(object):
    def threeSumClosest(self, nums, target):
        # [-1, 2, 1, -4]
        nums.sort()  # [-4, -1, 1, 2]
        temp = 999999 # max num
        for i in range (len(nums)-2):
            f = i + 1
            e = len(nums)-1
            while f < e:
                sum = nums[i] + nums[f] + nums[e]
                if abs(sum - target) < temp:
                    temp = abs(sum - target)
                    result = sum
                if sum > target:
                    e = e - 1
                if sum < target:
                    f = f + 1
                if sum == target:
                    if f < e:
                        return nums[i] + nums[f] +nums[e] 
        return result





