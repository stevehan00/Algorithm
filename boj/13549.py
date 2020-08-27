import heapq

n, k = map(int, input().split())

heap = [(0, n)]
visited = [False]*(100000+1)
ans = 0
visited[n] = True

while heap:
    time, node = heapq.heappop(heap)

    if node == k:
        ans = time
        break

    elif k < node:
        heapq.heappush(heap, (time+1, node-1))
    else:
        if node*2 <= 100000 and visited[node*2] == False:
            heapq.heappush(heap, (time, node*2))
            visited[node*2] = True
        if node-1 >= 0 and visited[node-1] == False:
            heapq.heappush(heap, (time+1, node-1))
            visited[node-1] = True
        if node+1 <= 100000 and visited[node+1] == False:
            heapq.heappush(heap, (time+1, node+1))
            visited[node+1] = True

        

print(ans)