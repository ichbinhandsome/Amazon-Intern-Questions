'''
Given a list of positive integers nums and an int target, return indices of the two numbers such that they add up to a target - 30.

Conditions:

You will pick exactly 2 numbers.
You cannot pick the same element twice.
If you have muliple pairs, select the pair with the largest number.
Example 1:

Input: nums = [1, 10, 25, 35, 60], target = 90
Output: [2, 3]
Explanation:
nums[2] + nums[3] = 25 + 35 = 60 = 90 - 30
Example 2:

Input: nums = [20, 50, 40, 25, 30, 10], target = 90
Output: [1, 5]
Explanation:
nums[0] + nums[2] = 20 + 40 = 60 = 90 - 30
nums[1] + nums[5] = 50 + 10 = 60 = 90 - 30
You should return the pair with the largest number.
'''

def findnum(nums, target):
    ans = [-1, -1]
    target -= 30
    hash_map = {}
    maximum = -1
    if not nums: return []
    for i in range(len(nums)):
        if target - nums[i] not in hash_map:
            hash_map[nums[i]] = i
        else:
            if nums[i] > maximum or target-nums[i] > maximum:
                ans[0], ans[1] = hash_map[target-nums[i]], i
                maximum = max(nums[i], target-nums[i])
    if ans == [-1,-1]: return []
    return ans

#test case
print(findnum([20, 50, 40, 25, 30, 10], 90))
print(findnum([1, 10, 25, 35, 60], 90))
print(findnum([50, 20, 10, 40, 25, 30], 90))
print(findnum([90, 85, 75, 60, 120,110,110, 150, 125] , 250))
print(findnum([90, 85, 75, 60, 120, 150, 125], 5))