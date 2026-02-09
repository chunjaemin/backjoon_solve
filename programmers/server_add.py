
players = [0, 2, 3, 3, 1, 2, 0, 0, 0, 0, 4, 2, 0, 6, 0, 4, 2, 13, 3, 5, 10, 0, 1, 5]
m = 3 
k = 5 
def solution(players, m, k):
    N = len(players)
    cur_server = [1] * N
    add_cnt = 0 
    
    for i in range(N):
        if cur_server[i] * m <= players[i]:
            need = (players[i] // m + 1) - cur_server[i]
            add_cnt += need 
            for di in range(k):
                if i + di < N:
                    cur_server[i + di] += need
    print(cur_server)
    return add_cnt

print(solution(players, m, k))