# Contains Duplicate II

**Difficulty:** Easy  
**Topics:** Array, Hash Table, Sliding Window  
**LeetCode URL:** [Contains Duplicate II](https://leetcode.com/problems/contains-duplicate-ii/)

## Problem Description

<p>Given an integer array <code>nums</code> and an integer <code>k</code>, return <code>true</code> <em>if there are two <strong>distinct indices</strong> </em><code>i</code><em> and </em><code>j</code><em> in the array such that </em><code>nums[i] == nums[j]</code><em> and </em><code>abs(i - j) &lt;= k</code>.</p>

<p>&nbsp;</p>

## Examples

<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [1,2,3,1], k = 3
<strong>Output:</strong> true
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [1,0,1,1], k = 1
<strong>Output:</strong> true
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> nums = [1,2,3,1,2,3], k = 2
<strong>Output:</strong> false
</pre>

## Constraints

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>-10<sup>9</sup> &lt;= nums[i] &lt;= 10<sup>9</sup></code></li>
	<li><code>0 &lt;= k &lt;= 10<sup>5</sup></code></li>
</ul>

## Solution

```python3
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
```

---
<div align="center">

**🔄 Synced with [CommitSync](https://www.google.com/search?q=CommitSync+extension)**

*Automatically organized and synced by CommitSync.*

</div>
