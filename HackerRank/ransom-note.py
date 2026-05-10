# Ransom Note

# Given two stings ransomNote and magazine, return true if ransomNote can be constructed from
# magazine and false otherwise.
# Each letter in magazine can only be used once in ransomNote.

# Runtime: 76 ms, faster than 47.27% of Python online submissions for Ransom Note.
# Memory Usage: 13.6 MB, less than 56.59% of Python online submissions for Ransom Note.

Each letter in magazine can only be used once in ransomNote.
class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        m = {}
        
        # construct map m
        for c in magazine:
            if m.has_key(c):
                m[c] += 1
            else:
                m[c] = 1
                
        for c in ransomNote:
            if not m.has_key(c) or m[c] == 0:
                return False
            m[c] -= 1
            
        return True

