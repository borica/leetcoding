# Duplicate Integer
# Solved 
# Given an integer array nums, return true if any value appears more than once in the array, otherwise return false.

# Example 1:

# Input: nums = [1, 2, 3, 3]

# Output: true
# Example 2:

# Input: nums = [1, 2, 3, 4]

# Output: false

# https://neetcode.io/problems/duplicate-integer

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        unique = []

        for i in range(len(nums)):
            if nums[i] in unique:
                return True

            unique.append(nums[i])
        
        return False
