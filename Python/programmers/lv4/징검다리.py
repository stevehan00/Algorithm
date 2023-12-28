def solution(distance, rocks, n):
    rocks.sort()
    left, right = 1, distance
    ans = 0
    
    while left <= right:
        mid = (left + right) // 2
        mins = 1000000001
        
        cnt = 0
        cur_r = 0
        for c in rocks:
            if c - cur_r < mid:
                cnt += 1
            else:
                mins = min(mins, c-cur_r)
                cur_r = c
        print(mid, cnt) 
        if cnt > n:
            right = mid - 1
        else:
            ans = mins
            left = mid + 1
    
    return ans