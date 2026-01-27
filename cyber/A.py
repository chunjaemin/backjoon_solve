import sys
input = sys.stdin.readline

ans = ""
N = int(input())
for i in range(N):
    a, b = input().split()
    b = int(b)
    
    if b == 2026:
        ans = a 
        
print(ans)