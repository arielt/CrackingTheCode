# Given a string containing digits from 2-9 inclusive,
# return all possible letter combinations that the number could represent.
# Return the answer in any order.

# A mapping of digit to letters (just like on the telephone buttons) is given below.
# Note that 1 does not map to any letters.

class Solution:
    map = {
        '2': ['a','b','c'],
        '3': ['d', 'e', 'f'],
        '4': ['g', 'h', 'i'],
        '5': ['j', 'k', 'l'],
        '6': ['m', 'n', 'o'],
        '7': ['p', 'q', 'r', 's'],
        '8': ['t', 'u', 'v'],
        '9': ['w', 'x', 'y', 'z']
    }
    
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []
        
        if len(digits) == 1:
            return self.map[digits[0]]
        
        rv = []
        t = self.letterCombinations(digits[1:])
        for c in self.map[digits[0]]:
            for suf in t:
                rv.append(c + suf)
        return rv

