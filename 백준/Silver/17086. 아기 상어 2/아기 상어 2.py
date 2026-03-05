import sys
from collections import deque 
input = sys.stdin.readline 


R, C = [-1,-1,-1,0,0,1,1,1], [-1,0,1,-1,1,-1,0,1]
N, M = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(N)]

ans = 0
for sr in range(N):
    for sc in range(M):
        if board[sr][sc] == 1:
            continue
        q = deque()
        q.append((sr, sc))
        visited = [[-1]* M for _ in range(N)]
        visited[sr][sc] = 0 

        while q:
            r, c = q.popleft()
            
            if board[r][c] == 1 and visited[r][c] > 0:
                ans = max(ans, visited[r][c])
                break 
            
            for i in range(8):
                nr, nc = r + R[i], c + C[i]
                if 0<=nr<N and 0<=nc<M:
                    if visited[nr][nc] == -1:
                        q.append((nr, nc))
                        visited[nr][nc] = visited[r][c] + 1 
        # print(sr, sc)
        # for row in visited:
        #     print(row)
print(ans)