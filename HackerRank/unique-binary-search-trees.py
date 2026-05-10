# Given n, how many structurally unique BST's (binary search trees) that store values 1 ... n?

# It requires some explanation. Dynamic programming array (dp) will have number of structurally
# unique BSTs at dp[n].
# For any given i, dp[i] will be sum of all possible combinations (j running from 1 to i),
# where j is chosen to be a root
# and number of unique BSTs in a left subtree multiplied by number of unique BSTs in a right
# subtree: dp[j-1]*dp[i-j]

class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [0] * (n+1)
        dp[0] = 1
        for i in range(1, n+1):
            for j in range(1, i+1):
                dp[i] += dp[j-1]*dp[i-j]
        return dp[n]

