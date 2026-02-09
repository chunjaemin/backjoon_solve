import sys
input = sys.stdin.readline 

N = 10 
score = [5,3,7,5,3,3,3,6,1,8,7]
ans = 0 

for i in range(N):
    scc = 0 
    score[i] = -1 
    
    for x in range(N):
        next = (N + 1 + x) % N
        prev = (N - 1 + x) % N
        if score[x] > score[next] and score[x] > score[prev]:
            scc += 1 
    ans = max(ans, scc)
print(ans)