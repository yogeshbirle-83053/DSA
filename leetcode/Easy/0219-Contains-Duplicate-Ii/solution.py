# LeetCode Problem: Contains Duplicate II
# Link: https://leetcode.com/problems/contains-duplicate-ii/
# Difficulty: Easy
# Language: python3

class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:

        # n = len(nums)
        # low = 0
        # high = 1
        # check = False
        # while high < n:
        #     if nums[low] == nums[high]:
        #          sub = high- low
                 
        #          if sub <= k:
        #             check = True
        #             return True

        #     high+=1

        # if check == False:
        #     return False
        seen = {}

        for i in range(len(nums)):
            if nums[i] in seen:
                if  i - seen[nums[i]] <= k:
                    return True

        
            seen[nums[i]]= i
        
        return False


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna