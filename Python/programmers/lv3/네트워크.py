def solution(n, computers):
    answer = 0
    visited = set()
    
    def dfs(s):
        print('test')
        stk = [s]
        visited.add(s)
        while stk:
            cur = stk.pop()
            
            for i in range(n):
                if computers[cur][i] == 1 and i not in visited:
                    stk.append(i)
                    visited.add(i)
            
    for i in range(n):
        if i not in visited:
            answer += 1
            dfs(i)

    return answer