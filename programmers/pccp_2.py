
#파라메트릭 서치로 푸는 문제 

def solution(diffs, times, limit):
    N = len(diffs)
    
    def parametric(level):
        use_time = 0 
        for i in range(N):
            if diffs[i] <= level:
                use_time += times[i]
            else:
                if i-1 >= 0:
                    prev_time = times[i-1]
                else:
                    prev_time = 0 
                r_time = (diffs[i] - level) * (prev_time + times[i])
                c_time = times[i]
                use_time += r_time + c_time 
        
            if use_time > limit:
                return False 
        # print(use_time, limit)
        return True 
    
    l, r = 1, max(diffs)
    while l <= r:
        m = (l+r) // 2

        if parametric(m):
            r = m - 1
        else:
            l = m + 1 
    
    return l

diffs = [1, 5, 3]
times = [2, 4, 7]
limit = 30
print(solution(diffs, times, limit))