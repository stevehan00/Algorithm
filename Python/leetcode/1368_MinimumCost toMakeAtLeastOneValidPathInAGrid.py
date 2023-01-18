import heapq, sys

class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        INF = sys.maxsize
        dp = [[INF]*n for _ in range(m)]
        dp[0][0] = 0
        pq = []
        
        heapq.heappush(pq, (0, 0, 0))
        
        dr = [0,0,1,-1]
        dc = [1,-1,0,0]
        
        while pq:
            cur = heapq.heappop(pq)
            if cur[1] == m-1 and cur[2] == n-1:
                return cur[0]
            
            for i in range(4):
                next_r = cur[1] + dr[i]
                next_c = cur[2] + dc[i]
                
                if (0 <= next_r < m and 0 <= next_c < n):
                    cost = 1
                    if i == grid[cur[1]][cur[2]]-1:
                        cost = 0
                    
                    if dp[next_r][next_c] > cur[0] + cost:
                        dp[next_r][next_c] = cur[0] + cost
                        heapq.heappush(pq, (cur[0] + cost, next_r, next_c))
