# LeetCode Problem: Kids With the Greatest Number of Candies
# Link: https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/
# Difficulty: Easy
# Language: python3

class Solution:
    def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:

        maximum = max(candies)
        result = []

        for candi in candies:
            if candi + extraCandies >= maximum:
                result.append(True)
            else:
                result.append(False)
        return result
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna