# On a staircase, the i-th step has some non-negative cost cost[i] assigned (0 indexed).
# Once you pay the cost, you can either climb one or two steps. You need to find minimum cost to reach the top of the floor, and you can either start from the step with index 0, or the step with index 1.
class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        l = len(cost)        
        res = [None] * l
        res[0] = cost[0]
        res[1] = cost[1]
        for i in range (2, l):
            res[i] = cost[i] + min(res[i-1], res[i-2])
        return min(res[l-1], res[l-2])

