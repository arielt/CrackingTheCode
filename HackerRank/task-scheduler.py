# Task Scheduler
# https://leetcode.com/problems/task-scheduler/

from collections import Counter

class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """        
        count = Counter(tasks).most_common()
        most_frequent = count[0][1] - 1
        idle = most_frequent * n
        
        for i in range (1,len(count)):
            idle -= min(count[i][1], most_frequent) # min required for elements with most frequency
            if idle < 0:
                idle = 0
                break
        
        return len(tasks) + idle

