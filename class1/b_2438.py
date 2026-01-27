import sys
input = sys.stdin.readline

N = int(input())

for i in range(1, N+1):
    a = ""
    for j in range(N):
        if j >= N-i:
            a += "*"
        else:
            a+= " "
    print(a)