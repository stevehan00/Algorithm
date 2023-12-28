from collections import defaultdict

def solution(tickets):
    graph = defaultdict(list)
    
    for a,b in tickets:
        graph[a].append(b)
    for k in graph.keys():
        graph[k].sort(reverse=True)

    st = ["ICN"]
    path = []
    
    while st:
        top = st[-1]
        
        if top not in graph or len(graph[top]) == 0:
            path.append(st.pop())
        else:
            st.append(graph[top].pop())
    
    ans = path[::-1]
    
    return ans