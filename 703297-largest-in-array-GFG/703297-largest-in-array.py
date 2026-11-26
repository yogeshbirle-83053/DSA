class Solution:
    def largest(self, arr):
        
        largest = float('-inf')
        
        for i in range(len(arr)):
            if largest < arr[i]:
                largest = arr[i]
        
        return largest
            
        # code here
        


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna