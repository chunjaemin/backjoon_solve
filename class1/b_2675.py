import sys
input = sys.stdin.readline

N = int(input())

for i in range(N):
    a, b = input().split()
    a= int(a)
    b = list(b)
    
    ans = ""
    for x in b:
        for i in range(a):
            ans += x
    print(ans)