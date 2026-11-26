# LeetCode Problem: Two Sum
# Link: https://leetcode.com/problems/two-sum/
# Difficulty: Easy
# Language: python3

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:

        hashmap = {}

        for i in range(len(nums)):
            check = target - nums[i]

            if check in hashmap:
                return [hashmap[check],i]

            hashmap[nums[i]] = i
            

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna