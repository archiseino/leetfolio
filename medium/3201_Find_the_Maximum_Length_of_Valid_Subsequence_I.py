"""
Leet code problem 3201: Find the Maximum Length of Valid Subsequence I
https://leetcode.com/problems/find-the-maximum-length-of-valid-subsequence-i/

Approach: Using dynamic programming to keep track of the maximum lengths of subsequences
There are four buckets:
1. Odd subsequence length
2. Even subsequence length
3. Alternating odd subsequence length
4. Alternating even subsequence length

Time Complexity: O(n)
Space Complexity: O(1)
"""

class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        dp = [0, 0, 0, 0] # odd, even, alt-odd, alt-even

        for num in nums:
            odd = num % 2 == 1

            # Copy the dp as the backup bucket
            prev = dp[:]
            if odd:
                dp[0] = prev[0] + 1
                # Max bucket on whether the prev was even, if so, then add to the bucket
                dp[2] = max(prev[2], prev[3] + 1, 1)

            else :
                dp[1] = prev[1] + 1
                # Same thing but for the even, if prev is odd, add to the bucket
                dp[3] = max(prev[3], prev[2] + 1, 1)
        
        return max(dp)
                