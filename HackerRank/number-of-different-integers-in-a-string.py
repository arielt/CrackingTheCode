# Number of Different Integers in a String

# You are given a string word that consists of digits and lowercase English letters.

# You will replace every non-digit character with a space. For example, "a123bc34d8ef34" will become " 123  34 
# 8  34". Notice that you are left with some integers that are separated by at least one space: "123", "34", 
# "8", and "34".

# Return the number of different integers after performing the replacement operations on word.

# Two integers are considered different if their decimal representations without any leading zeros are 
# different.

# Test results

# Runtime: 24 ms, faster than 51.74% of Python online submissions for Number of Different Integers in a 
# String.

# Memory Usage: 13.7 MB, less than 25.58% of Python online submissions for Number of Different Integers in a 
# String.

class Solution(object):
    def numDifferentIntegers(self, word):
        """
        :type word: str
        :rtype: int
        """
        c = {} # dict of integers
        curr = '' # current number
        
        for i in range(len(word)):
            if word[i].isnumeric():
                curr += word[i]
            else:
                # word[i] = 'x'
                if curr != '':
                    c[int(curr)] = True
                    curr = ''
        
        if curr != '':
                    c[int(curr)] = True

        return len(c)

