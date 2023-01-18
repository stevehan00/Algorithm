from collections import defaultdict
import heapq

def solution(s1, s2, k):

    parent = defaultdict(set)
    graph = defaultdict(set)

    for i in range(len(s1)):
        graph[s1[i]].add(s2[i])
        parent[s2[i]].add(s1[i])

    find = [k] 
    road = set()
    p = set()

    while find:
        cur = find.pop()

        road.add(cur)

        if len(parent[cur]) == 0:
            p.add(cur)

        for c in parent[cur]:
            find.append(c)

    q = []
    path = [] # answer
    visit = set()

    for c in p:
        heapq.heappush(q, c)

    while q:
        cur = heapq.heappop(q)
        visit.add(cur) 
        path.append(cur)

        if cur == k:
            break

        for c in graph[cur]:
            flag = True

            if c not in visit and c in road:
                for g in parent[c]:
                    if g not in visit:
                        flag = False
                        break

                if flag:
                    heapq.heappush(q, c)

    return path