from collections import Counter
class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:


        # dp[i][j] will store the maximum subset size with at most i 0's and j 1's
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for s in strs:
            # Count the number of '0's and '1's in the current string
            zero_count, one_count = Counter(s)['0'], Counter(s)['1']

            # Update dp in reverse order to avoid reusing the same string
            for i in range(m, zero_count - 1, -1):
                for j in range(n, one_count - 1, -1):
                    dp[i][j] = max(dp[i][j], dp[i - zero_count][j - one_count] + 1)

        return dp[m][n]
                    

        