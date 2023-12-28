import heapq

def solution(jobs):
    jobs.sort(key = lambda x : x[0])
    pq = []
    
    answer = 0
    idx = 0
    time = 0
    lens = len(jobs)
    
    while idx < lens or pq:
        while idx < lens and jobs[idx][0] <= time:
            heapq.heappush(pq, (jobs[idx][1], jobs[idx][0]))
            idx += 1
        
        if not pq:
            time = jobs[idx][0]
        else:
            job = heapq.heappop(pq)
            answer += (time-job[1]) + job[0]
            time += job[0]
    
    return answer//lens