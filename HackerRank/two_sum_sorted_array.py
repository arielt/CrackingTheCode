# Given an array of integers that is already sorted in ascending order,
# find two numbers such that they add up to a specific target number.
class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        s = 0
        e = len(numbers) - 1
        while s < e:
            t = numbers[s] + numbers[e]
            if t == target:
                return [s+1, e+1]
            if t > target:
                e-=1
            else:
                s+=1

