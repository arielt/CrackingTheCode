# Given a set of non-overlapping intervals, insert a new interval
# into the intervals (merge if necessary).

# You may assume that the intervals were initially sorted according
# to their start times.


class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        if len(intervals) == 0:
            return [newInterval]

        state = 0
        rv = []
        curr = []

        s = newInterval[0]
        e = newInterval[1]
        for i in intervals:
            # print "i", i
            if state == 0:  # no overlap yet
                if s > i[1]:  # didn't reach yet
                    rv.append(i)
                    continue
                if e < i[0]:  # first interval
                    rv.append(newInterval)
                    rv.append(i)
                    state = 2
                    continue
                curr = [min(s, i[0]), max(e, i[1])]
                # print "curr", curr
                state = 1
                continue

            if state == 1:  # overlapping
                if curr[1] >= i[0]:  # overlap continues
                    curr = [min(curr[0], i[0]), max(curr[1], i[1])]
                    continue
                rv.append(curr)
                curr = []
                rv.append(i)
                state = 2
                continue

            if state == 2:  # finishing
                rv.append(i)

        if state == 0:
            rv.append(newInterval)
        elif state == 1 and len(curr):
            rv.append(curr)

        return rv

