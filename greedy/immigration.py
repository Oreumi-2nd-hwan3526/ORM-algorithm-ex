# boj_3079

def solution(n, times):
    answer = 0
    end = min(times)
    start = max(times)*n
    while start <= end:
        mid = (start+ end) // 2
        checked = 0
        for time in times:
            checked += mid // time
            if checked >= n:
                break
        
        if checked >= n:
            answer = mid
            end = mid - 1
        elif checked < n:
            start = mid + 1
            
    return answer