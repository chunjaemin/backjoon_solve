import sys
from collections import deque 
input = sys.stdin.readline 

def debug_b(board):
    for row in board:
        print(" ".join(map(str, row)))

N = 6
board = [
    ['B','O','B','B','B','B'],
    ['X','X','X','X','X','B'],
    ['B','B','O','B','P','B'],
    ['X','X','B','X','B','B'],
    ['B','B','O','X','B','B'],
    ['B','B','B','B','B','B']
]

target = []
S, E = -1 ,-1
for r in range(N):
    for c in range(N):
        if board[r][c] == 'O':
            target.append((r, c))
        elif board[r][c] == 'P':
            S, E = r, c 
             
R, C = [0,0,1,-1], [1,-1,0,0]
def bfs(t):
    q = deque()
    visited = [[-1] * N for _ in range(N)]
    
    q.append((S, E))
    visited[S][E] = 0 
    while q:
        r, c = q.popleft()
        if r == t[0] and c == t[1]:
            # debug_b(visited)
            return visited[r][c]
            
        for i in range(4):
            nr, nc = r + R[i], c + C[i]
            if 0<= nr < N and 0<= nc < N:
                if visited[nr][nc] == -1 and board[nr][nc] != 'X':
                    q.append((nr, nc))
                    visited[nr][nc] = visited[r][c] + 1                            

ans = 0
for i in range(len(target)):
    # print(target[i])
    # print(bfs(target[i]))
    ans= max(ans, bfs(target[i]))

print(ans)
        