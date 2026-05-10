# Given a list of non negative integers, arrange them such that they form the largest number.

# Convert numbers to strings and sort using comparators that concatenates and compares two strings.


class Solution(object):        
    def comparator(self, x, y):
        return int(y+x) - int(x+y)

    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        largest = ''.join(sorted(map(str, nums), cmp=self.comparator))
        if largest[0] == '0':
            return '0'
        return largest

