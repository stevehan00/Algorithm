def solution(n, times):
    left, right = 1, n*max(times)
    answer = 0
    while left <= right:
        mid = (left + right) // 2

        cnt = 0
        for c in times:
            cnt += mid//c
            if cnt >= n:
                break
        
        if cnt >= n:
            right = mid - 1
            answer = mid
        else:
            left = mid + 1
    
    return answer