class Solution:
    def minSubarraySum(self, arr: list[int]) -> int:
        # code here
        
        i = 0
        current_sum = arr[0]
        min_sum = arr[0]
        
        for i in range(1,len(arr)):
            
            current_sum = min(arr[i], current_sum+arr[i])
            min_sum = min(current_sum,min_sum)
        
        return min_sum
            
            

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna