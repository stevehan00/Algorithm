from collections import Counter

def solution(begin, target, words):
    if target not in words:
        return 0
    
    stk = [(begin,0)]
    visited = set()
    visited.add(begin)
    
    while stk:
        cur, cnt = stk.pop()
        cur_b = Counter(list(cur))
        
        if cur == target:
            return cnt
        
        for c in words:
            if c not in visited:
                if len(Counter(list(c)) - cur_b) == 1:
                    stk.append((c, cnt+1))
                    visited.add(c)
    
    return 0