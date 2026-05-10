# Count Items Matching a Rule

# You are given an array items, where each items[i] = [typei, colori, namei] describes the type, color, and 
# name of the ith item. You are also given a rule represented by two strings, ruleKey and ruleValue.

# The ith item is said to match the rule if one of the following is true:

# ruleKey == "type" and ruleValue == typei.
# ruleKey == "color" and ruleValue == colori.
# ruleKey == "name" and ruleValue == namei.
# Return the number of items that match the given rule.

# Test Results

# Runtime: 200 ms, faster than 79.65% of Python online submissions for Count Items Matching a Rule.
# Memory Usage: 21 MB, less than 58.20% of Python online submissions for Count Items Matching a Rule.

class Solution(object):
    def countMatches(self, items, ruleKey, ruleValue):
        """
        :type items: List[List[str]]
        :type ruleKey: str
        :type ruleValue: str
        :rtype: int
        """
        keys = {
            'type': 0,
            'color': 1,
            'name': 2
        }
        
        rc = 0
        
        for i in items:
            if i[keys[ruleKey]] == ruleValue:
                rc += 1
                
        return rc

