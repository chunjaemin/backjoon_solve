import sys
input = sys.stdin.readline


max = 0 
idx = 0 
for i in range(9):
    n = int(input())
    if max <= n:
        max = n
        idx = i+1
        
print(max)
print(idx) 