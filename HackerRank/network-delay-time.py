# There are N network nodes, labelled 1 to N.

# Given times, a list of travel times as directed edges times[i] = (u, v, w), where u is the source node,
# is the target node, and w is the time it takes for a signal to travel from source to target.

# Now, we send a signal from a certain node K. How long will it take for all nodes to receive the signal?
# If it is impossible, return -1.
class Solution(object):
    def networkDelayTime(self, times, N, K):
        """
        :type times: List[List[int]]
        :type N: int
        :type K: int
        :rtype: int
        """
        # Essentially, it is Dijkstra.
        graph = collections.defaultdict(list)
        for (u, v, w) in times:
            graph[u].append((v,w))

        graph = {}
        for (u, v, w) in times:
            if graph.has_key(u):
              graph[u].append((v,w))
            else:
                graph[u] = [(v,w)]
            
        dist = {K: 0}
        pq = [(0, K)]
        
        while len(pq) > 0:
            weight, node = heapq.heappop(pq)
            if graph.has_key(node):
              for v,w in graph[node]:
                if not dist.has_key(v) or dist[v] > weight + w:
                  dist[v] = weight + w
                  heapq.heappush(pq, (dist[v], v))
        
        if  len(dist) < N:
            return -1
        else:
            return max(dist.values())

