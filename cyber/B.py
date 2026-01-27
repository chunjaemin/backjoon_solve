import sys
input = sys.stdin.readline

N = int(input())

arr = list(map(int,input().split()))

ans = 1
for i in range(N-1):
    if arr[i] >= arr[i+1]:
        ans = 0 

print(ans)