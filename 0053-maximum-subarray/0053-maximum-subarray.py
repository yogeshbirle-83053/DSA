class Solution:
    def maxSubArray(self, nums: list[int]) -> int:

        i = 0
        current_sum = nums[0]
        max_sum = nums[0]

        for i in range(1,len(nums)):
            n1 = current_sum + nums[i]
            n2 = nums[i]

            current_sum = max(n1,n2)

            max_sum = max(current_sum,max_sum)
        
        return max_sum
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna