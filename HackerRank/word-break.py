# Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, determine if s can be segmented into a space-separated sequence of one or more dictionary words.

class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        if not s: return False
        if not wordDict: return False
        
        words = set(wordDict)
        lens = set()
        for w in words:
            lens.add(len(w))
        
        sl = len(s)
        dp = [False] * (sl + 1)
        dp[0] = True
        
        for i in range(1, (sl + 1)):
            for l in lens:
                if i>=l and dp[i-l] and s[i-l:i] in words:
                    dp[i] = True
                    break
        return dp[sl]

