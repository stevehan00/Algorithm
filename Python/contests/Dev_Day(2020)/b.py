from collections import defaultdict, deque

def solution(n, t1, t2):
    answer = []

    graph = defaultdict(list)
    group = []

    for i in range(len(t1)):
        graph[t1[i]].append(t2[i])
        graph[t2[i]].append(t1[i])

    visit = set()

    def bfs(start):
        lst = [start]
        q = deque()
        q.append(start)

        while q:
            cur = q.popleft()

            for c in graph[cur]:
                if c not in visit:
                    q.append(c)
                    visit.add(c)
                    lst.append(c)
        return lst

    for i in range(1,n+1):
        if i not in graph:
            answer.append(i)
            continue

        if i not in visit:
            visit.add(i)
            temp = sorted(bfs(i))
            answer.append(temp[(len(temp)-1)//2])

    return sorted(answer)