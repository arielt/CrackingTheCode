# https://leetcode.com/problems/roman-to-integer

class Solution:
    def romanToInt(self, s: str) -> int:
        conv = {
            'M': 1000,
            'D': 500,
            'C': 100,
            'L': 50,
            'X': 10,
            'V': 5,
            'I': 1
        }

        sum = 0
        for i in range(len(s)-1):
            if conv[s[i]] < conv[s[i + 1]]:
                sum -= conv[s[i]]
            else:
                sum += conv[s[i]]
        
        return sum + conv[s[-1]]

