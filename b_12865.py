import sys
input = sys.stdin.readline 

N, W = map(int, input().split())

items = [] 
for i in range(N):
    w, v = map(int, input().split())
    items.append((w,v))

dp = [[0] * N for _ in range(W+1)]

for i in range(len(items)):
    # w, v = items[i]
    # if w + 
    pass